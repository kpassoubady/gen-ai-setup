# CLAUDE.md

## Project overview

Pre-class setup repository for the "Generative AI: Prompt Engineering for Software Developers" 4-day training course. Contains OS-specific install guides (macOS, Windows) and a self-contained verification project (`test-setup/`) that confirms the student's environment works end to end before Day 1.

## Related repositories

| Repo | Path | Purpose |
| :--- | :--- | :--- |
| gen-ai | `../gen-ai` | Instructor-led 4-day course (slides, labs, demos, diagrams) |
| building-with-llms-book | `../building-with-llms-book` | Book manuscript: 14 chapters, appendices, PDF/EPUB build |
| building-with-llms-companion | `../building-with-llms-companion` | Book companion: exercises, solutions, capstone projects |

The `test-setup/llm_client.py` in this repo mirrors the pattern in `gen-ai/shared/llm_client.py` and `building-with-llms-companion/shared/llm_client.py`. Keep provider models and API patterns in sync across all three.

## Repository structure

```
gen-ai-setup/
  README.md              Root landing page with quick-start checklist
  install-mac.md         macOS install guide (Homebrew, Python, Git, VS Code, AI assistant)
  install-win.md         Windows install guide (same steps, Windows-native commands)
  test-setup/
    .env.example         Template for LLM credentials (gateway or personal key)
    requirements.txt     All Python packages used across the 4-day course
    llm_client.py        Provider-agnostic LLM client (openai, gemini, claude, azure gateway)
    hello_llm.py         Verification script: prints config, makes one live LLM call
    README.md            Detailed steps and troubleshooting for the verification project
```

## Key conventions

- Markdown files use plain hyphens (`-`), never em dashes or en dashes.
- No horizontal rules (`---`) as section dividers; headings provide structure.
- Bold is reserved for headings and table headers, not mid-paragraph emphasis.
- Code blocks use `bash` for macOS/Linux and `cmd` for Windows commands.
- The `.env` file is gitignored; `.env.example` is the committed template.

## Tech stack

- Python 3.11+ (3.12 recommended)
- litellm for provider-agnostic LLM routing
- Providers: OpenAI, Gemini, Claude, Azure-OpenAI gateway
- Key packages: openai, tiktoken, numpy, faiss-cpu, flask, jupyter

## LLM client pattern

`test-setup/llm_client.py` reads `LLM_PROVIDER` from `.env` and routes through litellm. The `azure` provider supports corporate gateways using a bearer token (`AZURE_AD_TOKEN`) or a standard API key (`AZURE_API_KEY`). No code changes needed to switch providers.

## Common tasks

- Edit install guides: update `install-mac.md` or `install-win.md`, keep both in sync for shared sections (API config, AI assistant options, troubleshooting).
- Add a new AI assistant option: add a subsection under "AI Coding Assistant Setup" in both install guides and update the table in `README.md`.
- Add a Python package: add to `test-setup/requirements.txt` with a minimum version pin.
- Update provider models: edit `PROVIDER_MODELS` in `test-setup/llm_client.py`.

## Linting

Markdown linting is configured via `.markdownlint.json` (most rules disabled for flexibility). Run with `markdownlint` if available.
