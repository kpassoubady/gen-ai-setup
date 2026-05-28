"""
Hello LLM — pre-class setup verification.

Confirms your environment can reach the LLM and get a real response.
A clean run here means you are ready for Day 1.

Steps:
1. Copy .env.example to .env and fill in your values
       macOS/Linux:  cp .env.example .env
       Windows:      copy .env.example .env
2. Install dependencies
       pip install -r requirements.txt
3. Run this script
       python3 hello_llm.py        (Windows: python hello_llm.py)
"""

import sys

from llm_client import get_completion_full, show_config


def main():
    print("=" * 60)
    print("Gen-AI Course — Setup Verification")
    print("=" * 60)

    print("\n[1/2] Configuration")
    show_config()

    print("\n[2/2] Live LLM call (tier='mini')")
    try:
        response = get_completion_full(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Reply with a one-sentence hello for a class setup test."},
            ],
            tier="mini",
            max_tokens=50,
        )
    except Exception as err:  # noqa: BLE001 — surface any setup failure clearly
        print("\n❌ SETUP FAILED — the LLM call did not succeed.\n")
        print(f"Error: {type(err).__name__}: {err}\n")
        print("Checklist:")
        print("  - Did you copy .env.example to .env and fill in real values?")
        print("  - Is LLM_PROVIDER set to the provider you have access to?")
        print("  - For the gateway: are AZURE_API_BASE and AZURE_AD_TOKEN correct?")
        print("  - Did 'pip install -r requirements.txt' complete without errors?")
        sys.exit(1)

    content = response.choices[0].message.content
    usage = response.usage

    print(f"Response: {content}")
    print(f"Tokens:   {usage.prompt_tokens} in + {usage.completion_tokens} out")

    print("\n" + "=" * 60)
    print("✅ SETUP VERIFIED — you are ready for Day 1!")
    print("=" * 60)


if __name__ == "__main__":
    main()
