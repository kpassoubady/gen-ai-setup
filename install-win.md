# Generative AI: Prompt Engineering for Software Developers - Windows Install

This guide walks through the complete development environment setup on Windows 10/11 for the 4-day training course.

## 1. Install Python

Download from <https://www.python.org/downloads/> (3.12 recommended).

**During installation:**

- Check **"Add Python to PATH"**
- Choose **"Customize installation"** and keep pip enabled

Verify in Command Prompt or PowerShell:

```cmd
python --version
pip --version
```

Expected: Python 3.11+.

Upgrade pip:

```cmd
python -m pip install --upgrade pip
```

## 2. Install Git

Download from <https://git-scm.com/download/win> and install with default options.

Verify:

```cmd
git --version
```

Configure (use your name and email):

```cmd
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 3. Install Visual Studio Code

Download from <https://code.visualstudio.com/download> and install.

**During installation:**

- Check **"Add to PATH"**
- Check **"Register Code as an editor for supported file types"**

Verify:

```cmd
code --version
```

### Recommended VS Code Extensions

Install from the Extensions panel (`Ctrl+Shift+X`) or via CLI:

```cmd
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension ms-python.debugpy
```

## 4. AI Coding Assistant Setup

> **Your instructor will confirm which tool your team will use.** Install only the one assigned to your team.

### Option A: GitHub Copilot

```cmd
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
- Install Node.js from <https://nodejs.org/> (LTS version), then:

```cmd
npm install -g @anthropic-ai/claude-code
```

- Authenticate with your Anthropic account:

```cmd
claude
```

- For detailed setup, see the [Claude Helper](https://github.com/kpassoubady/claude-helper).

## 5. Get the Setup Project & Install Packages

Clone the setup repository :

```cmd
git clone https://github.com/kpassoubady/gen-ai-setup.git %USERPROFILE%\gen-ai-setup
cd %USERPROFILE%\gen-ai-setup\test-setup
```

Create and activate a virtual environment:

```cmd
python -m venv .venv
.venv\Scripts\activate
```

> **PowerShell users:** If activation fails, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` first, then use `.venv\Scripts\Activate.ps1`.

Install every course package:

```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 6. Configure API Access

The setup project ships a `.env.example` template. Copy it and fill in your values:

```cmd
copy .env.example .env
```

Open `.env` and configure the provider your team uses. Most teams use the gateway (no personal API key needed):

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

## 7. Verify Everything Works

Run the hello-LLM check. It makes one real call and confirms the full stack works:

```cmd
python hello_llm.py
```

A successful run ends with:

```text
✅ SETUP VERIFIED. You are ready for Day 1!
```

If it fails, see the troubleshooting table in [`test-setup/README.md`](./test-setup/README.md) or section 9 below.

## 8. Jupyter Notebook Verification

```cmd
REM Run from the test-setup directory you set up above
REM (if you opened a new terminal, cd back into it first).
.venv\Scripts\activate
jupyter notebook
```

Create a new Python 3 notebook and run:

```python
import openai, tiktoken, numpy
print("All imports successful. You are ready for class!")
```

## 9. Troubleshooting

| Issue | Solution |
|-------|---------|
| `python` is not recognized | Re-run installer with "Add Python to PATH" checked, or add manually via System Properties → Environment Variables |
| `pip` is not recognized | Run `python -m ensurepip --upgrade` |
| `code` is not recognized | Re-run VS Code installer with "Add to PATH" checked |
| PowerShell: "running scripts is disabled" | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| OpenAI API returns `401` | Check your API key in `.env` and remove any extra spaces or quotes |
| `faiss-cpu` install fails | Try `pip install faiss-cpu --no-cache-dir` or use `chromadb` as alternative |
| `chromadb` install fails on older Windows | Ensure Visual C++ Build Tools are installed: <https://visualstudio.microsoft.com/visual-cpp-build-tools/> |
| Virtual environment not activating | Use `.venv\Scripts\activate` (cmd) or `.venv\Scripts\Activate.ps1` (PowerShell) |
| Copilot not suggesting | Check license status at <https://github.com/settings/copilot> |
| Cursor/Windsurf not connecting | Ensure you are signed in and have an active subscription |
| Long path errors | Enable long paths: run as admin `reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f` and restart |

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

You are ready for Day 1!
