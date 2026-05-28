"""
Unified LLM client — setup verification copy.

This mirrors shared/llm_client.py from the course repo so a successful run
here guarantees the same code path works in class. Set your provider and
credentials in `.env` (copy from `.env.example`); no code changes needed.

Supported providers:
  - openai   → GPT-4o, GPT-4o-mini
  - gemini   → Gemini 2.5 Flash, Gemini 2.0 Flash
  - claude   → Claude Sonnet 4, Claude Haiku 4.5
  - azure    → Azure-OpenAI-style gateway (custom endpoint + bearer token)

The `azure` provider lets students who only have access to a corporate
gateway (no personal API key) run everything unchanged. The deployment name,
endpoint, and version are all read from `.env`, so the model can change
without touching any code.
"""

import os
from dotenv import load_dotenv
import litellm

load_dotenv()

# Provider-to-model mapping. For azure, deployment names come from .env.
PROVIDER_MODELS = {
    "openai": {
        "default": "gpt-4o",
        "mini": "gpt-4o-mini",
    },
    "gemini": {
        "default": "gemini/gemini-2.5-flash",
        "mini": "gemini/gemini-2.0-flash",
    },
    "claude": {
        "default": "claude-sonnet-4-20250514",
        "mini": "claude-haiku-4-5-20251001",
    },
    "azure": {
        "default": os.getenv("AZURE_DEPLOYMENT_DEFAULT", "gpt-4o"),
        "mini": os.getenv(
            "AZURE_DEPLOYMENT_MINI",
            os.getenv("AZURE_DEPLOYMENT_DEFAULT", "gpt-4o"),
        ),
    },
}

# Read from .env — defaults to openai
PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()


def get_model(tier="default"):
    """Get the model string for the active provider."""
    models = PROVIDER_MODELS.get(PROVIDER)
    if not models:
        raise ValueError(
            f"Unknown provider '{PROVIDER}'. "
            f"Set LLM_PROVIDER to one of: {list(PROVIDER_MODELS.keys())}"
        )
    name = models.get(tier, models["default"])
    # litellm routes to the gateway when the model is prefixed with "azure/".
    if PROVIDER == "azure" and not name.startswith("azure/"):
        return f"azure/{name}"
    return name


def _provider_kwargs():
    """Extra litellm kwargs for the active provider.

    For the azure gateway, this supplies the endpoint, API version, and
    bearer token so the request matches the verified Postman call:
        {api_base}/openai/deployments/{deployment}/chat/completions?api-version=...
        Authorization: Bearer <token>
    """
    if PROVIDER == "azure":
        kwargs = {
            "api_base": os.getenv("AZURE_API_BASE"),
            "api_version": os.getenv("AZURE_API_VERSION", "2024-02-01"),
            # azure_ad_token is sent as the "Authorization: Bearer" header.
            # Falls back to AZURE_API_KEY (sent as the "api-key" header) for
            # gateways that expect the standard Azure key instead.
            "azure_ad_token": os.getenv("AZURE_AD_TOKEN"),
            "api_key": os.getenv("AZURE_API_KEY"),
        }
        # Drop unset values so litellm doesn't see a None credential.
        return {k: v for k, v in kwargs.items() if v}
    return {}


def get_completion(messages, tier="default", temperature=0.7, max_tokens=1024, **kwargs):
    """Send a chat completion request to the active LLM provider.

    Returns the response message content as a string.
    """
    model = get_model(tier)
    response = litellm.completion(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        **_provider_kwargs(),
        **kwargs,
    )
    return response.choices[0].message.content


def get_completion_full(messages, tier="default", temperature=0.7, max_tokens=1024, **kwargs):
    """Same as get_completion() but returns the full response object."""
    model = get_model(tier)
    return litellm.completion(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        **_provider_kwargs(),
        **kwargs,
    )


def show_config():
    """Print the current LLM configuration — useful for environment checks."""
    print(f"Provider:      {PROVIDER}")
    print(f"Default model: {get_model('default')}")
    print(f"Mini model:    {get_model('mini')}")

    if PROVIDER == "azure":
        print(f"Gateway:       {os.getenv('AZURE_API_BASE', '⚠️  AZURE_API_BASE not set')}")
        print(f"API version:   {os.getenv('AZURE_API_VERSION', '2024-02-01')}")

    # Check the credential is set (without revealing it)
    key_vars = {
        "openai": "OPENAI_API_KEY",
        "gemini": "GEMINI_API_KEY",
        "claude": "ANTHROPIC_API_KEY",
        "azure": "AZURE_AD_TOKEN",
    }
    key_var = key_vars.get(PROVIDER, "UNKNOWN")
    key_value = os.getenv(key_var, "")
    if not key_value and PROVIDER == "azure":
        key_var, key_value = "AZURE_API_KEY", os.getenv("AZURE_API_KEY", "")
    if key_value:
        print(f"Credential:    {key_var} = ...{key_value[-4:]}")
    else:
        print(f"Credential:    ⚠️  {key_var} is NOT set")


if __name__ == "__main__":
    show_config()
