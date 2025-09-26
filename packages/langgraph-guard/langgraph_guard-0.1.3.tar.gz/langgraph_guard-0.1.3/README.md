# Langgraph Guard

This package is required for integrating your Langchain based Agentic Application to Aryaka's AISecure Guard Service.

## What it does

`langgraph-guard` is a security middleware designed to seamlessly integrate with any LangGraph application, providing a critical layer of real-time security/content validation. It intercepts user inputs, LLM prompts and responses, tool I/O, retriever I/O, and final outputs via a LangGraph callback handler and asynchronously calls the AISecure GenAI Protect service. If this service identifies a policy violation, `langgraph-guard` immediately blocks the unsafe operation from continuing, preventing threats before they can impact the application.
 
Configuration is managed declaratively through environment variables, requiring no changes to the application's source code.
 
## Key Capabilities
- **Real-Time Threat Prevention:** Actively blocks malicious inputs, prevents sensitive data (PII) leakage, and ensures AI-generated content adheres to organizational safety standards.
- **Context-Aware Policies:** Applies granular security rules based on the specific user, their role, and the task being performed within the AI system.
- **Comprehensive Validation:** Leverages a powerful suite of validators including but not limited to:
- **Content & Safety:** Toxicity, sentiment, and content classification.
- **Privacy & Compliance (DLP):** PII detection and adherence to data protection standards.
- **Code Detection & Prompt Injection:** Detection of code snippets and potential prompt injection attacks.
- **Zero-Code Integration:** A fast, non-invasive way to add robust security and compliance controls to any LangGraph-based application

## Configuration (via environment variables)

All configuration is loaded from environment variables (e.g., from a `.env` file). At minimum, enable the guard and provide the service URL, default inspection object, stage mapping, and tenant/site identifiers.

Required when `GUARD_ENABLED=true`:
- `GUARD_URL`: Base URL of the AI Secure Validation API. 
- `GUARD_DEFAULT_INSPECT`: Fallback inspection object name.
- `GUARD_STAGE_MAP`: JSON mapping that selects inspection objects by stage/group/user/hook.
- `GUARD_CUSTOMER_ID`: Customer ID
- `GUARD_TENANT_ID`: Tenant ID.
- `GUARD_SITE_ID`: Site ID.
- TLS either:
  - `GUARD_INSECURE_SKIP_VERIFY=true` (dev only), or
  - both `GUARD_CA_PATH` and `GUARD_CA_PEM` set for certificate verification.

Optional:
- `GUARD_JWT`: Bearer token for the guard service.
- `GUARD_USER_ID`: Default user id (if not provided at runtime).
- `GUARD_GROUPS`: JSON array of groups for policy resolution (e.g., `["analysts","admins"]`).

Example `.env` snippet:

```bash
GUARD_ENABLED=true
GUARD_URL=https://protect.example.com
GUARD_JWT=eyJhbGciOiJI... # optional
GUARD_DEFAULT_INSPECT=inspect_default
GUARD_STAGE_MAP={
  "stage:plan": {"pre_llm": "inspect_plan"},
  "group:analysts": {"pre_llm": "inspect_group"},
  "user:alice": {"final_output": "inspect_user"},
  "*": {"final_output": "inspect_default"}
}
GUARD_CUSTOMER_ID=ciid-123
GUARD_TENANT_ID=tenant-abc
GUARD_SITE_ID=site-001
# One of the following TLS setups
GUARD_INSECURE_SKIP_VERIFY=false
GUARD_CA_PATH=/etc/ssl/certs/ca-bundle.crt
GUARD_CA_PEM="-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----\n"
```

`GUARD_STAGE_MAP` shape (keys → hook → inspect name):
- Keys may be:
  - `stage:<name>` or just `<name>` for a workflow stage
  - `group:<name>` for group-based rule
  - `user:<id>` for user-specific rule
  - `*` wildcard for any stage
- Hooks supported by the handler:
  - `user_input`, `final_output`, `pre_llm`, `post_llm`, `pre_tool`, `post_tool`, `pre_mcp`, `post_mcp`, `error`

## How to use

You can attach the guard with zero code changes using environment variables, or explicitly in code.

### 1) Environment-driven (no code changes)
Wrap your LangGraph runnable factory with the provided decorator. The guard will read all settings from env and attach itself only if `GUARD_ENABLED=true` and required vars are present.

```python
from langgraph_guard import guard

@guard
def get_app():
    # build and return your LangGraph runnable
    return app
```

Alternatively, if you already have an `app` instance:

```python
from langgraph_guard import attach_guard_from_env

app = attach_guard_from_env(app)
```

### 2) Programmatic attach (custom config objects)
If you centralize config in your app, you can pass that object to attach based on its attributes:

```python
from langgraph_guard import attach_guard_if_enabled

class AppConfig:
    guard_enabled = True
    guard_url = "https://protect.example.com"
    guard_jwt = "..."  # optional
    guard_default_inspect = "inspect_default"
    guard_customer_id = "ciid-123"
    guard_tenant_id = "tenant-abc"
    guard_site_id = "site-001"
    guard_ca_path = "/etc/ssl/certs/ca-bundle.crt"
    guard_ca_pem = None
    guard_insecure_skip_verify = False
    # Optional identity defaults
    guard_user_id = "anonymous"
    guard_groups = ["analysts"]

# Ensure GUARD_STAGE_MAP is provided via environment
app = attach_guard_if_enabled(app, AppConfig())
```
