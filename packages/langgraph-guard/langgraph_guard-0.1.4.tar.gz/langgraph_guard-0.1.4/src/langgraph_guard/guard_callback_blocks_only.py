"""AsyncGuardHandler implementation for GenAI Protect integration with LangGraph.

This module provides comprehensive security validation for all LangGraph components
through callback handlers that integrate with the GenAI Protect API service.
"""

from __future__ import annotations

import ssl
import json
import uuid as _uuid
import datetime
import re
import ast
from typing import Any, Dict, List, Optional, Union

import httpx
from pydantic import BaseModel, Field, HttpUrl

from langchain_core.callbacks import AsyncCallbackHandler
from langchain_core.outputs import LLMResult


# =============================================================================
# CONFIGURATION MODELS
# =============================================================================

class GuardServiceConfig(BaseModel):
    """Configuration for connecting to the Guard validation API service.
    
    This configuration targets the FastAPI server exposed by `api_server.py`
    and its `/v1.0/validate` endpoint for content validation.
    """
    service_url: HttpUrl
    jwt: Optional[str] = None  # Guard JWT for GenAI Protect authentication
    ca_cert_path: Optional[str] = None
    ca_cert_pem: Optional[str] = None
    timeout_s: float = 15.0
    insecure_skip_verify: bool = False


class Identity(BaseModel):
    """User identity model for policy resolution and access control."""
    user_id: str
    account_id: Optional[str] = None
    groups: List[str] = Field(default_factory=list)
    roles: List[str] = Field(default_factory=list)


class PolicyKey(BaseModel):
    """Policy matching key for inspection object selection."""
    user_id: Optional[str] = None
    group: Optional[str] = None
    stage: Optional[str] = None
    hook: Optional[str] = None


class PolicyRule(BaseModel):
    """Policy rule mapping a key pattern to an inspection object."""
    key: PolicyKey
    inspect_name: str


class GuardPolicy(BaseModel):
    """Policy engine for selecting appropriate inspection objects based on context."""
    """This is not referenced."""
    rules: List[PolicyRule] = Field(default_factory=list)
    default_inspect_name: Optional[str] = None

    def resolve(self, identity: Identity, stage: Optional[str], hook: str) -> str:
        """Select the most specific inspection object for the current validation context."""
        best_inspect = None
        best_score = -1
        user_groups = set(identity.groups or [])
        
        for rule in self.rules:
            score = 0
            if rule.key.user_id and rule.key.user_id == identity.user_id:
                score += 8
            if rule.key.group and rule.key.group in user_groups:
                score += 4
            if rule.key.stage and rule.key.stage == stage:
                score += 2
            if rule.key.hook and rule.key.hook == hook:
                score += 1
            if score > best_score:
                best_score = score
                best_inspect = rule.inspect_name
        
        if best_inspect:
            return best_inspect
        if self.default_inspect_name:
            return self.default_inspect_name
        raise RuntimeError("No inspection object could be resolved from policy")


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def _hook_to_validate_type(hook: str) -> str:
    """Map callback hook to validate.type expected by the guard API."""
    mapping = {
        "user_input": "prompt",
        "pre_llm": "prompt",
        "post_llm": "response",
        "pre_tool": "text",
        "post_tool": "text",
        "pre_mcp": "text",
        "post_mcp": "text",
        "final_output": "response",
        "error": "text",
        # explicit agent mappings
        "agent_action": "text",
        "agent_finish": "response",
    }
    return mapping.get(hook, "text")


# =============================================================================
# ASYNC GUARD HANDLER
# =============================================================================

class AsyncGuardHandler(AsyncCallbackHandler):
    """Comprehensive Guard interceptor for security validation in LangGraph."""
    
    def __init__(self, service: GuardServiceConfig, identity: Identity,
                 policy: GuardPolicy, *, ciid: str, default_tsid: Optional[str] = None,
                 default_sid: Optional[str] = None, correlation_seed: Optional[str] = None):
        self.service = service
        self.identity = identity
        self.policy = policy
        self.ciid = ciid
        self.default_tsid = default_tsid
        self.default_sid = default_sid
        self._client: Optional[httpx.AsyncClient] = None
        self.application_name: Optional[str] = None
        self.root_run_id: Optional[str] = None
        # Cache for deduplication (key: hash of text+context, value: verdict)
        self._validation_cache: Dict[str, str] = {}
        # Correlation (parallel-safe)
        self._session_uuid: str = str(_uuid.uuid4())
        self._correlation_seed = correlation_seed
        self._corr_by_root_key: Dict[str, str] = {}   # root_key -> correlation_id
        self._rootkey_by_run: Dict[str, str] = {}     # run_id -> root_key

    # ------------------------------
    # TEXT EXTRACTION HELPERS
    # ------------------------------
    def _extract_text_from_content_parts(self, parts: Any) -> str:
        if parts is None:
            return ""
        if isinstance(parts, str):
            # Try to interpret repr-like strings and peel out content/tool calls
            from_repr = self._extract_from_repr_like_string(parts)
            return from_repr if from_repr else parts

        texts: List[str] = []
        if isinstance(parts, list):
            for p in parts:
                if isinstance(p, dict):
                    p_type = p.get("type")
                    if "text" in p:
                        texts.append(str(p["text"]))
                    elif p_type in {"input_text", "output_text", "tool_result"} and "content" in p:
                        texts.append(str(p["content"]))
                    elif p_type in {"json_object"} and ("json" in p or "content" in p):
                        payload = p.get("json", p.get("content"))
                        try:
                            texts.append(json.dumps(payload, ensure_ascii=False))
                        except Exception:
                            texts.append(str(payload))
                else:
                    t = getattr(p, "text", None) or getattr(p, "content", None)
                    if t:
                        texts.append(str(t))
                    else:
                        texts.append(self._to_str(p))
        else:
            try:
                return self._to_str(parts)
            except Exception:
                return str(parts)

        return "\n".join([t for t in texts if t])

    def _extract_function_and_tool_calls(self, msg: Any) -> str:
        """Pull function_call / tool_calls from message object OR dict."""
        out: List[str] = []

        # Object-style
        addl = getattr(msg, "additional_kwargs", None)
        tool_calls = getattr(msg, "tool_calls", None)
        if isinstance(addl, dict):
            # old OpenAI function_call
            fc = addl.get("function_call")
            if fc:
                out.append(f"[function_call name={fc.get('name')} args={fc.get('arguments')}]")
            tool_calls = tool_calls or addl.get("tool_calls")

        # Dict-style fallback
        if isinstance(msg, dict):
            addl = msg.get("additional_kwargs") if addl is None else addl
            if isinstance(addl, dict):
                fc = addl.get("function_call")
                if fc:
                    out.append(f"[function_call name={fc.get('name')} args={fc.get('arguments')}]")
                tool_calls = tool_calls or addl.get("tool_calls")
            tool_calls = tool_calls or msg.get("tool_calls")

        # Normalize & render any tool calls
        if tool_calls:
            try:
                for tc in tool_calls:
                    name = tc.get("name")
                    args = tc.get("args") or tc.get("arguments")
                    # legacy {'function': {'name','arguments'}}
                    if (not name) and isinstance(tc.get("function"), dict):
                        fn = tc["function"]
                        name = fn.get("name", name)
                        args = args or fn.get("args") or fn.get("arguments")
                    out.append(f"[tool_call name={name} args={args}]")
            except Exception:
                # Best-effort stringify
                out.append(f"[tool_calls {self._to_str(tool_calls)}]")

        return "\n".join(out)

    def _extract_from_message(self, msg: Any) -> str:
        """Support HumanMessage/AIMessage/SystemMessage/ToolMessage/ChatMessage or dict-ish."""
        # Dict-like message
        if isinstance(msg, dict):
            if "content" in msg:
                text = self._extract_text_from_content_parts(msg.get("content"))
            else:
                text = ""
            calls = self._extract_function_and_tool_calls(msg)
            return f"{text}\n{calls}".strip() if calls and text else (calls or text)

        # Object-like message
        content = getattr(msg, "content", None)
        text = self._extract_text_from_content_parts(content)
        calls = self._extract_function_and_tool_calls(msg)
        if calls:
            return f"{text}\n{calls}" if text else calls
        return text

    def _extract_from_messages_param(self, messages: Any) -> str:
        if not messages:
            return ""

        # parallel prompts: list of sequences
        if isinstance(messages, list) and messages and isinstance(messages[0], list):
            seq_texts = []
            for seq in messages:
                parts = [self._extract_from_message(m) for m in seq]
                seq_texts.append("\n".join([p for p in parts if p]))
            return "\n\n---\n\n".join([s for s in seq_texts if s])

        if isinstance(messages, list):
            parts = []
            for m in messages:
                if isinstance(m, str):
                    parts.append(self._extract_from_repr_like_string(m) or m)
                else:
                    parts.append(self._extract_from_message(m))
            return "\n".join([p for p in parts if p])

        if isinstance(messages, str):
            return self._extract_from_repr_like_string(messages) or messages

        return self._to_str(messages)

    def _extract_from_llm_result(self, res: LLMResult) -> str:
        blocks: List[str] = []
        gens = getattr(res, "generations", []) or []
        for gen_list in gens:
            for gen in gen_list:
                if hasattr(gen, "text") and gen.text:
                    blocks.append(gen.text)
                elif hasattr(gen, "message"):
                    blocks.append(self._extract_from_message(gen.message))
                else:
                    # Sometimes providers stuff repr-like blobs in .text or .message
                    raw = self._to_str(gen)
                    parsed = self._extract_from_repr_like_string(raw)
                    blocks.append(parsed or raw)
        return "\n\n".join([b for b in blocks if b])

    def _extract_from_documents(self, documents: Any) -> str:
        if not documents:
            return ""
        parts: List[str] = []
        for d in documents:
            text = getattr(d, "page_content", None)
            parts.append(str(text) if text is not None else self._to_str(d))
        return "\n\n".join([p for p in parts if p])

    def _extract_from_agent_action(self, action: Any) -> str:
        tname = getattr(action, "tool", None) or (action.get("tool") if isinstance(action, dict) else None)
        tinput = getattr(action, "tool_input", None) or (action.get("tool_input") if isinstance(action, dict) else None)
        log = getattr(action, "log", None) or (action.get("log") if isinstance(action, dict) else None)
        pieces = []
        if tname:
            pieces.append(f"[agent.tool] {tname}")
        if tinput is not None:
            pieces.append(self._to_str(tinput))
        if log:
            pieces.append(str(log))
        return "\n".join([p for p in pieces if p])

    def _extract_from_agent_finish(self, finish: Any) -> str:
        rv = getattr(finish, "return_values", None) or (finish.get("return_values") if isinstance(finish, dict) else {}) or {}
        log = getattr(finish, "log", None) or (finish.get("log") if isinstance(finish, dict) else None)
        out = rv.get("output")
        pieces = []
        if out is not None:
            pieces.append(self._to_str(out))
        elif rv:
            pieces.append(self._to_str(rv))
        if log:
            pieces.append(str(log))
        return "\n".join([p for p in pieces if p])

    # -------- REPR-LIKE STRING EXTRACTION (used only at boundaries) -----------

    _CONTENT_RE = re.compile(
        r"""content\s*=\s*(?P<q>['"])(?P<val>(?:\\.|(?!\1).)*?)\1""",
        re.DOTALL
    )
    _ADDL_RE = re.compile(r"""additional_kwargs\s*=\s*(\{.*?\})""", re.DOTALL)
    _TOOL_CALLS_RE = re.compile(r"""tool_calls\s*=\s*(\[[\s\S]*?\])""", re.DOTALL)

    def _extract_from_repr_like_string(self, s: str) -> str:
        """Parse repr-like dumps; ONLY used by chain start/end boundaries."""
        if not s or not isinstance(s, str):
            return ""

        pieces: List[str] = []

        # 1) All content='...' hits
        for m in self._CONTENT_RE.finditer(s):
            raw = m.group("val")
            try:
                txt = bytes(raw, "utf-8").decode("unicode_escape")
            except Exception:
                txt = raw
            txt = txt.strip()
            if txt:
                pieces.append(txt)

        # 2) additional_kwargs={...} with 'tool_calls'
        for m in self._ADDL_RE.finditer(s):
            block = m.group(1)
            try:
                data = ast.literal_eval(block)
                tc = data.get("tool_calls")
                if isinstance(tc, list) and tc:
                    pieces.append(self._render_tool_calls(tc))
            except Exception:
                pass

        # 3) tool_calls=[...] at top-level (or nested)
        for m in self._TOOL_CALLS_RE.finditer(s):
            block = m.group(1)
            try:
                tc = ast.literal_eval(block)
                if isinstance(tc, list) and tc:
                    pieces.append(self._render_tool_calls(tc))
            except Exception:
                pass

        return "\n".join([p for p in pieces if p]).strip()

    def _render_tool_calls(self, tool_calls: List[Dict[str, Any]]) -> str:
        lines: List[str] = []
        for tc in tool_calls:
            name = tc.get("name")
            args = tc.get("args") or tc.get("arguments")
            if not name and isinstance(tc.get("function"), dict):
                fn = tc["function"]
                name = fn.get("name", name)
                args = args or fn.get("args") or fn.get("arguments")
            lines.append(f"[tool_call name={name} args={args}]")
        return "\n".join(lines)

    def _extract_from_arbitrary_inputs(self, obj: Any) -> str:
        """Boundary extractor used at on_chain_start / on_chain_end only."""
        if obj is None:
            return ""
        if isinstance(obj, str):
            parsed = self._extract_from_repr_like_string(obj)
            return parsed if parsed else obj
        if isinstance(obj, (int, float, bool)):
            return str(obj)
        if isinstance(obj, dict):
            collected: List[str] = []
            for k in ("messages", "chat_history", "message"):
                if k in obj and obj[k] is not None:
                    collected.append(self._extract_from_messages_param(obj[k]))
            for k, v in obj.items():
                if k in {"prompt", "query", "question", "input", "text"} and isinstance(v, (str, list, dict)):
                    if isinstance(v, str):
                        parsed = self._extract_from_repr_like_string(v)
                        collected.append(parsed if parsed else v)
                    else:
                        collected.append(self._to_str(v) if isinstance(v, (dict, list)) else str(v))
            if not collected:
                for _, v in obj.items():
                    s = self._extract_from_arbitrary_inputs(v)
                    if s:
                        collected.append(s)
            return "\n".join([c for c in collected if c])
        if isinstance(obj, list):
            parts = []
            for x in obj:
                if isinstance(x, str):
                    parts.append(self._extract_from_repr_like_string(x) or x)
                else:
                    parts.append(self._extract_from_arbitrary_inputs(x))
            return "\n".join([p for p in parts if p])
        return self._to_str(obj)

    # ---- Correlation helpers (parallel-safe) --------------------------------

    _ID_KEYS = (
        "langgraph_request_id",
        "thread_id",
        "graph_id",
        "assistant_id",
        "user_id",
        "run_id",
        "parent_run_id",
        "root_run_id",
        "conversation_id",
        "request_id",
        "trace_id",
        "checkpoint_ns",
        "langgraph_checkpoint_ns",
    )

    _ID_REGEX = re.compile(
        r'"(?P<k>langgraph_request_id|thread_id|graph_id|assistant_id|user_id|run_id|parent_run_id|root_run_id|conversation_id|request_id|trace_id|checkpoint_ns|langgraph_checkpoint_ns)"\s*:\s*"(?P<v>[^"]+)"'
    )

    def _harvest_ids_from_text(self, text: str) -> Dict[str, str]:
        found: Dict[str, str] = {}
        if not text:
            return found
        snippet = text.strip()

        if snippet and snippet[0] in "{[":
            try:
                obj = json.loads(snippet)
                def walk(o):
                    if isinstance(o, dict):
                        for k, v in o.items():
                            if k in self._ID_KEYS and isinstance(v, (str, int)):
                                found[k] = str(v)
                            walk(v)
                    elif isinstance(o, list):
                        for it in o:
                            walk(it)
                walk(obj)
            except Exception:
                pass

        for m in self._ID_REGEX.finditer(snippet[:5000]):
            k = m.group("k")
            v = m.group("v")
            if k and v and k not in found:
                found[k] = v
        return found

    def _derive_root_key(
        self,
        raw_metadata: Optional[Dict[str, Any]],
        run_id: Optional[Union[str, _uuid.UUID]],
        parent_run_id: Optional[Union[str, _uuid.UUID]],
        text: str,
    ) -> str:
        md = raw_metadata or {}
        for k in ("langgraph_request_id", "thread_id"):
            v = md.get(k)
            if v:
                return f"{k}:{v}"

        tuple_parts = []
        for k in ("graph_id", "assistant_id", "user_id"):
            v = md.get(k)
            if v:
                tuple_parts.append(f"{k}={v}")
        if tuple_parts:
            return "tuple:" + "|".join(tuple_parts)

        ids_from_text = self._harvest_ids_from_text(text)
        for k in ("langgraph_request_id", "thread_id"):
            if k in ids_from_text:
                return f"{k}:{ids_from_text[k]}"

        pid = str(parent_run_id) if parent_run_id else None
        rid = str(run_id) if run_id else None
        if pid and pid in self._rootkey_by_run:
            return self._rootkey_by_run[pid]
        if rid and rid in self._rootkey_by_run:
            return self._rootkey_by_run[rid]

        anchor = pid or rid or self._session_uuid
        return f"run:{anchor}"

    def _correlation_id_for_event(
        self,
        raw_metadata: Optional[Dict[str, Any]],
        run_id: Optional[Union[str, _uuid.UUID]],
        parent_run_id: Optional[Union[str, _uuid.UUID]],
        text: str,
    ) -> str:
        root_key = self._derive_root_key(raw_metadata, run_id, parent_run_id, text)
        if run_id:
            self._rootkey_by_run[str(run_id)] = root_key
        if parent_run_id:
            self._rootkey_by_run.setdefault(str(parent_run_id), root_key)

        cid = self._corr_by_root_key.get(root_key)
        if not cid:
            base = f"{self._correlation_seed or ''}|{root_key}"
            cid = str(_uuid.uuid5(_uuid.NAMESPACE_URL, f"genaiprotect/langgraph/{base}"))
            self._corr_by_root_key[root_key] = cid
        return cid

    def reset_root(self) -> None:
        """Reset the handler state for a new conversation."""
        self.root_run_id = None
        self._validation_cache.clear()
        # Keep correlation maps for parallel runs.

    async def _get_client(self) -> httpx.AsyncClient:
        verify: Union[bool, str, ssl.SSLContext] = True
        if self.service.insecure_skip_verify:
            verify = False
        elif self.service.ca_cert_path:
            verify = self.service.ca_cert_path
        elif self.service.ca_cert_pem:
            ctx = ssl.create_default_context()
            ctx.load_verify_locations(cadata=self.service.ca_cert_pem)
            verify = ctx
        
        headers: Dict[str, str] = {}
        if self.service.jwt:
            headers["Authorization"] = f"Bearer {self.service.jwt}"
        
        base_url = str(self.service.service_url).rstrip('/')
        return httpx.AsyncClient(
            base_url=base_url,
            headers=headers,
            timeout=self.service.timeout_s,
            verify=verify,
        )
    
    def _maybe_set_root(self, run_id: Optional[str], parent_run_id: Optional[str]) -> None:
        if not self.root_run_id and run_id:
            self.root_run_id = parent_run_id or run_id
    
    def _to_str(self, value: Any) -> str:
        if value is None:
            return ""
        if isinstance(value, (str, int, float, bool)):
            return str(value)
        if isinstance(value, _uuid.UUID):
            return str(value)
        try:
            return json.dumps(value, ensure_ascii=False, default=str)
        except Exception:
            return str(value)
    
    def _create_cache_key(self, text: str, inspect_name: str, 
                          stage: Optional[str], hook: str, user_id: str) -> str:
        import hashlib
        text_sample = text[:1000] if len(text) > 1000 else text
        content = f"{text_sample}|{inspect_name}|{stage or ''}|{hook}|{user_id}"
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
    
    async def _validate(self, *, text: str, stage: Optional[str], hook: str,
                       run_id: Optional[str], parent_run_id: Optional[str],
                       tags: Optional[List[str]], metadata: Optional[Dict[str, Any]]) -> None:
        # DEBUG logging (disabled by default)
        if False:
            with open("api_log", "a", encoding="utf-8") as f:
                timestamp = datetime.datetime.now().isoformat()
                f.write("=" * 80 + "\n")
                f.write(f"[{timestamp}] [DEBUG METADATA] Hook: {hook}, Stage: {stage}\n")
                f.write(f"Run ID: {run_id}\n")
                f.write(f"Parent Run ID: {parent_run_id}\n")
                f.write(f"Tags: {tags}\n")
                f.write("Raw metadata:\n")
                if metadata is None:
                    f.write("  None\n")
                else:
                    f.write(json.dumps(metadata, indent=2, default=str) + "\n")
                f.write("=" * 80 + "\n")
            
        if not text or not text.strip():
            return
        
        current_identity = self.identity
        inspect_name = self.policy.resolve(current_identity, stage, hook)

        raw_metadata = metadata if isinstance(metadata, dict) else {}
        correlation_id = self._correlation_id_for_event(raw_metadata, run_id, parent_run_id, text)

        cache_key = self._create_cache_key(text, inspect_name, stage, hook, current_identity.user_id)
        if cache_key in self._validation_cache:
            cached_verdict = self._validation_cache[cache_key]
            if cached_verdict != "pass":
                raise RuntimeError(f"Cached validation failure: {cached_verdict}")
            return
        
        validate_type = _hook_to_validate_type(hook)

        if self.application_name is None:
           self.application_name = raw_metadata.get("graph_id", None)
        
        meta: Dict[str, str] = {
            "hook": hook or "",
            "stage": stage or "",
            "correlation_id": correlation_id,
            "user_id": str(raw_metadata.get("user_id") or ""),
            "thread_id": str(raw_metadata.get("thread_id") or ""),
            "assistant_id": str(raw_metadata.get("assistant_id") or ""),
            "run_id": str(run_id) if run_id else "",
            "root_run_id": str(self.root_run_id) if self.root_run_id else "",
            "parent_run_id": str(parent_run_id) if parent_run_id else "",
            "langgraph_auth_user_id": str(raw_metadata.get("langgraph_auth_user_id") or ""),
            "langgraph_request_id": str(raw_metadata.get("langgraph_request_id") or ""),
            "langgraph_node": str(raw_metadata.get("langgraph_node") or ""),
            "langgraph_step": str(raw_metadata.get("langgraph_step") or ""),
            "langgraph_checkpoint_ns": str(raw_metadata.get("langgraph_checkpoint_ns") or ""),
            "checkpoint_ns": str(raw_metadata.get("checkpoint_ns") or ""),
            "search_api": str(raw_metadata.get("search_api") or ""),
            "model": str(raw_metadata.get("model") or ""),
            "tags": ",".join([str(t) for t in tags]) if tags else "",
            "supabase_access_token": str(raw_metadata.get("supabaseAccessToken") or ""),
        }
        
        tsid = (raw_metadata.get("guard_tsid") or raw_metadata.get("tsid") or 
               self.default_tsid or "default")
        sid = (raw_metadata.get("guard_sid") or raw_metadata.get("sid") or 
              self.default_sid or "default")
        
        payload = {
            "source": {
                "framework": "Langgraph",
                "application": self.application_name,
            },
            "content": {
                "type": validate_type,
                "text": text,
            },
            "genai_protect_config": {
                "config_instance_id": self.ciid,
                "inspection_object": inspect_name,
                "customer_id": tsid,
                "site_id": sid,
            },
            "metadata": meta,
        }
        
        client = await self._get_client()
        try:
            if False:
                with open("api_log", "a", encoding="utf-8") as f:
                    timestamp = datetime.datetime.now().isoformat()
                    f.write(f"[{timestamp}] [DEBUG] Payload: {json.dumps(payload, indent=2, default=str)}\n")
            
            response = await client.post("/v1.0/validate", json=payload)
            response.raise_for_status()
            
            data = response.json() if response.content else {}
            verdict = str(data.get("overallverdict", "fail")).lower()
            
            self._validation_cache[cache_key] = verdict
            
            if verdict != "pass":
                reason = data.get("message") or "Content blocked by guard"
                raise RuntimeError(reason)
            
        finally:
            await client.aclose()
    
    # =============================================================================
    # CALLBACK IMPLEMENTATIONS
    # =============================================================================
    
    async def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], *,
                            run_id: str, parent_run_id: Optional[str] = None, tags=None,
                            metadata=None, **_):
        """Validate user inputs when chains start (EXTRACTED)."""
        self._maybe_set_root(run_id, parent_run_id)
        text = self._extract_from_arbitrary_inputs(inputs)  # extraction ON at boundary
        stage = None
        if isinstance(metadata, dict):
            stage = metadata.get("stage")
        if not stage and isinstance(serialized, dict):
            stage = serialized.get("id") or serialized.get("name")
        if not stage:
            stage = "chain"
        
        await self._validate(
            text=text,
            stage=stage,
            hook="user_input",
            run_id=run_id,
            parent_run_id=parent_run_id,
            tags=tags,
            metadata=metadata
        )
    
    async def on_chain_end(self, outputs: Dict[str, Any], *, run_id: str,
                          parent_run_id: Optional[str] = None, tags=None,
                          metadata=None, **_):
        """Validate final outputs when chains complete (EXTRACTED)."""
        text = self._extract_from_arbitrary_inputs(outputs)  # extraction ON at boundary
        stage = None
        if isinstance(metadata, dict):
            stage = metadata.get("stage")
        if not stage:
            stage = "chain"
        
        await self._validate(
            text=text,
            stage=stage,
            hook="final_output",
            run_id=run_id,
            parent_run_id=parent_run_id,
            tags=tags,
            metadata=metadata
        )

    # -------------------- MID-PIPELINE: NO EXTRACTION, RAW STRINGS --------------------

    async def on_chat_model_start(self, serialized: Dict[str, Any], messages: List[List[Any]], *,
                                 run_id: str, parent_run_id: Optional[str] = None, tags=None,
                                 metadata=None, **_):
        """Validate prompts before chat model (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        stage = metadata.get("stage") if isinstance(metadata, dict) else None
        if not stage:
            stage = "llm"
        text = str(messages)  # raw
        await self._validate(text=text, stage=stage, hook="pre_llm",
                             run_id=run_id, parent_run_id=parent_run_id,
                             tags=tags, metadata=metadata)
    
    async def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], *,
                          run_id: str, parent_run_id: Optional[str] = None, tags=None,
                          metadata=None, **_):
        """Validate LLM prompts (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        stage = (metadata.get("stage") if isinstance(metadata, dict) else None) or "llm"
        text = str(prompts)  # raw
        await self._validate(text=text, stage=stage, hook="pre_llm",
                             run_id=run_id, parent_run_id=parent_run_id,
                             tags=tags, metadata=metadata)
    
    async def on_llm_end(self, response: LLMResult, *, run_id: str,
                        parent_run_id: Optional[str] = None, tags=None,
                        metadata=None, **_):
        """Validate LLM responses (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        stage = (metadata.get("stage") if isinstance(metadata, dict) else None) or "llm"
        text = str(response)  # raw
        await self._validate(text=text, stage=stage, hook="post_llm",
                             run_id=run_id, parent_run_id=parent_run_id,
                             tags=tags, metadata=metadata)
    
    async def on_tool_start(self, serialized: Dict[str, Any], input_str: str, *,
                           run_id: str, parent_run_id: Optional[str] = None, tags=None,
                           metadata=None, inputs: Optional[Dict[str, Any]] = None, **_):
        """Validate tool inputs (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        stage = (metadata.get("stage") if isinstance(metadata, dict) else None) or "tool"
        text = str(inputs if inputs is not None else input_str)  # raw
        await self._validate(text=text, stage=stage, hook="pre_tool",
                             run_id=run_id, parent_run_id=parent_run_id,
                             tags=tags, metadata=metadata)
    
    async def on_tool_end(self, output: Any, *, run_id: str,
                         parent_run_id: Optional[str] = None, tags=None,
                         metadata=None, **_):
        """Validate tool outputs (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        stage = (metadata.get("stage") if isinstance(metadata, dict) else None) or "tool"
        text = str(output)  # raw
        await self._validate(text=text, stage=stage, hook="post_tool",
                             run_id=run_id, parent_run_id=parent_run_id,
                             tags=tags, metadata=metadata)
    
    async def on_retriever_start(self, serialized: Dict[str, Any], query: str, *,
                                run_id: str, parent_run_id: Optional[str] = None,
                                tags=None, metadata=None, **_):
        """Validate retriever queries (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        stage = (metadata.get("stage") if isinstance(metadata, dict) else None) or "retriever"
        text = str(query)  # raw
        await self._validate(text=text, stage=stage, hook="pre_mcp",
                             run_id=run_id, parent_run_id=parent_run_id,
                             tags=tags, metadata=metadata)
    
    async def on_retriever_end(self, documents: List[Any], *, run_id: str,
                              parent_run_id: Optional[str] = None, tags=None,
                              metadata=None, **_):
        """Validate retriever results (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        stage = (metadata.get("stage") if isinstance(metadata, dict) else None) or "retriever"
        text = str(documents)  # raw
        await self._validate(text=text, stage=stage, hook="post_mcp",
                             run_id=run_id, parent_run_id=parent_run_id,
                             tags=tags, metadata=metadata)

    async def on_agent_action(self, action: Any, *, run_id: str,
                              parent_run_id: Optional[str] = None, tags: Optional[List[str]] = None, **_):
        """Validate agent actions (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        text = str(action)  # raw
        await self._validate(text=text, stage="agent", hook="agent_action",
                             run_id=run_id, parent_run_id=parent_run_id,
                             tags=tags, metadata=None)

    async def on_agent_finish(self, finish: Any, *, run_id: str,
                              parent_run_id: Optional[str] = None, tags: Optional[List[str]] = None, **_):
        """Validate agent final outputs (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        text = str(finish)  # raw
        await self._validate(text=text, stage="agent", hook="agent_finish",
                             run_id=run_id, parent_run_id=parent_run_id,
                             tags=tags, metadata=None)
    
    # =============================================================================
    # ERROR HANDLERS (RAW: no extraction)
    # =============================================================================
    
    async def on_llm_error(self, error: Exception, *, run_id: str,
                          parent_run_id: Optional[str] = None, tags=None,
                          metadata=None, **_):
        """Handle LLM errors (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        text = str(error)  # raw
        if len(text) > 100:
            stage = metadata.get("stage", "llm") if isinstance(metadata, dict) else "llm"
            await self._validate(text=text, stage=stage, hook="error",
                                 run_id=run_id, parent_run_id=parent_run_id,
                                 tags=tags, metadata=metadata)
    
    async def on_tool_error(self, error: Exception, *, run_id: str,
                           parent_run_id: Optional[str] = None, tags=None,
                           metadata=None, **_):
        """Handle tool errors (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        text = str(error)  # raw
        if len(text) > 100:
            stage = metadata.get("stage", "tool") if isinstance(metadata, dict) else "tool"
            await self._validate(text=text, stage=stage, hook="error",
                                 run_id=run_id, parent_run_id=parent_run_id,
                                 tags=tags, metadata=metadata)
    
    async def on_retriever_error(self, error: Exception, *, run_id: str,
                                parent_run_id: Optional[str] = None, tags=None,
                                metadata=None, **_):
        """Handle retriever errors (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        text = str(error)  # raw
        if len(text) > 100:
            stage = metadata.get("stage", "retriever") if isinstance(metadata, dict) else "retriever"
            await self._validate(text=text, stage=stage, hook="error",
                                 run_id=run_id, parent_run_id=parent_run_id,
                                 tags=tags, metadata=metadata)
    
    async def on_chain_error(self, error: Exception, *, run_id: str,
                            parent_run_id: Optional[str] = None, tags=None,
                            metadata=None, **_):
        """Handle chain errors (RAW, no extraction)."""
        self._maybe_set_root(run_id, parent_run_id)
        text = str(error)  # raw
        if len(text) > 100:
            stage = metadata.get("stage", "chain") if isinstance(metadata, dict) else "chain"
            await self._validate(text=text, stage=stage, hook="error",
                                 run_id=run_id, parent_run_id=parent_run_id,
                                 tags=tags, metadata=metadata)