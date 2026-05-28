# Generative AI: Prompt Engineering for Software Developers — macOS Install

This guide walks through the complete development environment setup on macOS for the 4-day training course.

---

## 1. Install Homebrew (if not already installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify:

```bash
brew --version
```

---

## 2. Install Python

```bash
brew install python
```

Verify:

```bash
python3 --version
pip3 --version
```

Expected: Python 3.11+ (3.12 recommended).

Upgrade pip:

```bash
pip3 install --upgrade pip
```

---

## 3. Install Git

```bash
brew install git
```

Verify:

```bash
git --version
```

Configure (use your name and email):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 4. Install Visual Studio Code

Download from <https://code.visualstudio.com/download> or install via Homebrew:

```bash
brew install --cask visual-studio-code
```

Verify the CLI is available:

```bash
code --version
```

### Recommended VS Code Extensions

Install from the Extensions panel (`Cmd+Shift+X`) or via CLI:

```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension ms-python.debugpy
```

---

## 5. AI Coding Assistant Setup

> **Your instructor will confirm which tool your team will use.** Install only the one assigned to your team.

### Option A: GitHub Copilot

```bash
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
```

- Sign in with your GitHub account that has an active Copilot license.
- Verify: open VS Code, type a comment in a `.py` file, and Copilot should suggest completions.
- For detailed setup, see the [GitHub Copilot Helper](https://github.com/kpassoubady/github-copilot-helper).

### Option B: Cursor

- Download and install from <https://cursor.com>.
- Cursor is a standalone editor (VS Code fork), so no separate extension is needed.
- Sign in with your Cursor account.
- For detailed setup, see the [Cursor Helper](https://github.com/kpassoubady/cursor-helper).

### Option C: Windsurf

- Download and install from <https://windsurf.com>.
- Windsurf is a standalone editor (VS Code fork), so no separate extension is needed.
- Sign in with your Windsurf account.
- For detailed setup, see the [Windsurf Helper](https://github.com/kpassoubady/windsurf-helper).

### Option D: Claude Code

- Claude Code runs in the terminal and works alongside any editor.
- Install via npm:

```bash
brew install node
npm install -g @anthropic-ai/claude-code
```

- Authenticate with your Anthropic account:

```bash
claude
```

- For detailed setup, see the [Claude Helper](https://github.com/kpassoubady/claude-helper).

---

## 6. Get the Setup Project & Install Packages

Clone the setup repository:

```bash
git clone https://github.com/kpassoubady/gen-ai-setup.git
cd ./gen-ai-setup/test-setup
```

Create and activate a virtual environment, then install every course package:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

---

## 7. Configure API Access

The setup project ships a `.env.example` template. Copy it and fill in your values:

```bash
cp .env.example .env
```

Open `.env` and configure the provider your team uses. **Most teams use the gateway (no personal API key needed):**

```text
LLM_PROVIDER=azure
AZURE_API_BASE=https://<your-gateway-host>/<path>
AZURE_API_VERSION=2024-02-01
AZURE_DEPLOYMENT_DEFAULT=gpt-4o
AZURE_DEPLOYMENT_MINI=gpt-4o-mini
AZURE_AD_TOKEN=<your bearer token>
```

> Your instructor provides the gateway URL and token. The model/deployment name
> may change before class, so just update `AZURE_DEPLOYMENT_DEFAULT`.
>
> Have a personal OpenAI key instead? Set `LLM_PROVIDER=openai` and
> `OPENAI_API_KEY=sk-...` (account needs ~$5 credit).

---

## 8. Verify Everything Works

Run the hello-LLM check. This installs nothing new. It makes one real call and confirms the full stack works:

```bash
python3 hello_llm.py
```

A successful run ends with:

```text
✅ SETUP VERIFIED. You are ready for Day 1!
```

If it fails, see the troubleshooting table in [`test-setup/README.md`](./test-setup/README.md) or section 10 below.

---

## 9. Jupyter Notebook Verification

```bash
# Run from the test-setup directory you set up above
# (if you opened a new terminal, cd back into it first).
source .venv/bin/activate
jupyter notebook --no-browser
```

Open the URL shown in the terminal. Create a new Python 3 notebook and run:

```python
import openai, tiktoken, numpy
print("All imports successful. You are ready for class!")
```

---

## 10. Troubleshooting

| Issue | Solution |
|-------|---------|
| `python3: command not found` | Run `brew install python` and restart terminal |
| `pip3: command not found` | Run `python3 -m ensurepip --upgrade` |
| `code: command not found` | Open VS Code → `Cmd+Shift+P` → "Shell Command: Install 'code' command in PATH" |
| OpenAI API returns `401` | Check your API key in `.env` and remove any extra spaces or quotes |
| `faiss-cpu` install fails | Try `pip3 install faiss-cpu --no-cache-dir` or use `chromadb` as alternative |
| Virtual environment not activating | Ensure you run `source .venv/bin/activate` (not `.venv\Scripts\activate`) |
| Copilot not suggesting | Check license status at <https://github.com/settings/copilot> |
| Cursor/Windsurf not connecting | Ensure you are signed in and have an active subscription |

---

## Summary

After completing this guide, you should have:

- Python 3.11+ with pip
- Git configured
- VS Code with Python extensions
- One AI coding assistant installed and authenticated
- All course Python packages installed in a virtual environment
- Gateway token (or personal API key) configured in `.env`
- `hello_llm.py` printing `✅ SETUP VERIFIED`
- Jupyter notebooks running

**You are ready for Day 1!**
