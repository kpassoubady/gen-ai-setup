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
| **Python Packages** | `openai`, `tiktoken`, `python-dotenv`, `numpy`, `faiss-cpu` or `chromadb`, `flask` or `fastapi`, `uvicorn`, `requests`, `jupyter` |
| **API Access** | OpenAI API key with credit |

> **Note:** Your instructor will confirm which AI coding assistant the team will use before the training. The core course content is the same regardless of the tool.

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

---

## Quick Verification Checklist

After completing the OS-specific install guide, confirm the following:

- [ ] `python3 --version` (or `python --version` on Windows) shows 3.11+
- [ ] `pip3 --version` (or `pip --version` on Windows) works
- [ ] `git --version` works
- [ ] `code --version` works (VS Code CLI)
- [ ] AI coding assistant extension is installed and authenticated in VS Code
- [ ] OpenAI API key is set in a `.env` file
- [ ] `python3 -c "import openai; print(openai.__version__)"` succeeds
- [ ] `python3 -c "import tiktoken; print(tiktoken.encoding_for_model('gpt-4o'))"` succeeds
- [ ] Jupyter notebook launches: `jupyter notebook --no-browser`

---

## Need Help?

If you encounter any issues during setup, please reach out to your instructor before the training day.
