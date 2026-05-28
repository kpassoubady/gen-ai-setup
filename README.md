# Generative AI: Prompt Engineering for Software Developers — Setup Guide

Pre-class installation instructions for the **Generative AI: Prompt Engineering for Software Developers** course.

Please complete the setup for your operating system **before the first day of class**.

---

## Installation Guides

Click on the link for your operating system to view the detailed setup guide.

| Platform | Installation Guide |
|----------|-------------------|
| **macOS** | [macOS Install Guide](./install-mac.md) |
| **Windows** | [Windows Install Guide](./install-win.md) |

---

## What You Will Install

| Category | Tools / Packages |
|----------|-----------------|
| **Language Runtime** | Python 3.11+ (3.12 recommended) |
| **Code Editor** | Visual Studio Code |
| **Version Control** | Git |
| **AI Coding Assistant** | One of: GitHub Copilot, Cursor, Windsurf, or Claude Code (instructor will confirm) |
| **Python Packages** | Installed from [`test-setup/requirements.txt`](./test-setup/requirements.txt) (`litellm`, `openai`, `tiktoken`, `python-dotenv`, `numpy`, `faiss-cpu`, `flask`, `requests`, `jupyter`) |
| **API Access** | A corporate LLM gateway token, **or** a personal OpenAI / Gemini / Claude key |

> **Note:** Your instructor will confirm which AI coding assistant the team will use before the training. The core course content is the same regardless of the tool.
>
> **No personal API key?** That is fine. The [`test-setup/`](./test-setup/) project supports a corporate gateway (Azure-OpenAI style) using a bearer token. Your instructor will provide the gateway URL and token.

---

## Verify Your Setup (Required)

After installing the tools below, run the self-contained verification project. A clean run means you are ready for class.

```bash
cd test-setup
python3 -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                   # Windows: copy .env.example .env
# edit .env with your gateway token (or personal API key)
python3 hello_llm.py
```

A successful run ends with `✅ SETUP VERIFIED`. See [`test-setup/README.md`](./test-setup/README.md) for details and troubleshooting.

---

## Quick Verification Checklist

After completing the OS-specific install guide, confirm the following:

- [ ] `python3 --version` (or `python --version` on Windows) shows 3.11+
- [ ] `pip3 --version` (or `pip --version` on Windows) works
- [ ] `git --version` works
- [ ] `code --version` works (VS Code CLI)
- [ ] AI coding assistant extension is installed and authenticated in VS Code
- [ ] Gateway token (or personal API key) is set in `test-setup/.env`
- [ ] `pip install -r test-setup/requirements.txt` completes without errors
- [ ] `python3 test-setup/hello_llm.py` prints `✅ SETUP VERIFIED`
- [ ] Jupyter notebook launches: `jupyter notebook --no-browser`

---

## Need Help?

If you encounter any issues during setup, please reach out to your instructor before the training day.

---

## AI Coding Assistant — Setup References

Depending on which tool your team uses, refer to the appropriate helper guide for detailed IDE-specific tips and configuration:

| Tool | Helper Reference |
|------|-----------------|
| **GitHub Copilot** | [GitHub Copilot Helper](https://github.com/kpassoubady/github-copilot-helper) |
| **Cursor** | [Cursor Helper](https://github.com/kpassoubady/cursor-helper) |
| **Windsurf** | [Windsurf Helper](https://github.com/kpassoubady/windsurf-helper) |
| **Claude Code** | [Claude Helper](https://github.com/kpassoubady/claude-helper) |

> These helper projects contain tool-specific shortcuts, configuration files, and usage guides that complement the course material.
