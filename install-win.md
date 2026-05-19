# Generative AI: Prompt Engineering for Software Developers — Windows Install

This guide walks through the complete development environment setup on Windows 10/11 for the 4-day training course.

---

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

---

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

---

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

---

## 4. AI Coding Assistant Setup

> **Your instructor will confirm which tool your team will use.** Install only the one assigned to your team.

### Option A: GitHub Copilot

```cmd
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
```

- Sign in with your GitHub account that has an active Copilot license.
- Verify: open VS Code, type a comment in a `.py` file — Copilot should suggest completions.
- For detailed setup, see the [GitHub Copilot Helper](https://github.com/kpassoubady/github-copilot-helper).

### Option B: Cursor

- Download and install from <https://cursor.com>.
- Cursor is a standalone editor (VS Code fork) — no separate extension needed.
- Sign in with your Cursor account.
- For detailed setup, see the [Cursor Helper](https://github.com/kpassoubady/cursor-helper).

### Option C: Windsurf

- Download and install from <https://windsurf.com>.
- Windsurf is a standalone editor (VS Code fork) — no separate extension needed.
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

---

## 5. OpenAI API Key Setup

1. Go to <https://platform.openai.com/api-keys> and create a new API key.
2. Ensure your account has at least **$5 credit** for lab exercises.
3. Store the key securely — never commit it to source control.

Create a `.env` file in your project directory. In PowerShell:

```powershell
"OPENAI_API_KEY=sk-your-key-here" | Out-File -Encoding utf8 .env
```

Or in Command Prompt:

```cmd
echo OPENAI_API_KEY=sk-your-key-here > .env
```

Verify the key works:

```cmd
python -c "from openai import OpenAI; from dotenv import load_dotenv; load_dotenv(); client = OpenAI(); r = client.chat.completions.create(model='gpt-4o-mini', messages=[{'role':'user','content':'Say hello in one word'}], max_tokens=10); print('API connection successful:', r.choices[0].message.content)"
```

---

## 6. Install Python Packages

Create and activate a virtual environment:

```cmd
mkdir %USERPROFILE%\gen-ai-course
cd %USERPROFILE%\gen-ai-course
python -m venv .venv
.venv\Scripts\activate
```

> **PowerShell users:** If activation fails, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` first, then use `.venv\Scripts\Activate.ps1`.

Create `requirements.txt` with the following content:

```text
openai>=1.30
tiktoken
python-dotenv
numpy
requests

# Day 3 — RAG
faiss-cpu
chromadb

# Day 3 — API wrapper
flask
fastapi
uvicorn[standard]

# Notebooks
jupyter
ipykernel

# Testing
pytest
```

Install all packages:

```cmd
pip install -r requirements.txt
```

Verify key packages:

```cmd
python -c "import openai; print('openai', openai.__version__)"
python -c "import tiktoken; print('tiktoken OK')"
python -c "import faiss; print('faiss OK')"
python -c "import chromadb; print('chromadb OK')"
python -c "import flask; print('flask', flask.__version__)"
python -c "import fastapi; print('fastapi OK')"
python -c "import numpy; print('numpy', numpy.__version__)"
```

---

## 7. Clone the Course Repository

Your instructor will provide the repository URL. Clone it:

```cmd
git clone <REPO_URL> %USERPROFILE%\gen-ai-course\repo
cd %USERPROFILE%\gen-ai-course\repo
```

Copy your `.env` file into the repo root:

```cmd
copy %USERPROFILE%\gen-ai-course\.env %USERPROFILE%\gen-ai-course\repo\.env
```

---

## 8. Jupyter Notebook Verification

```cmd
cd %USERPROFILE%\gen-ai-course
.venv\Scripts\activate
jupyter notebook
```

Create a new Python 3 notebook and run:

```python
import openai, tiktoken, numpy
print("All imports successful — you are ready for class!")
```

---

## 9. Troubleshooting

| Issue | Solution |
|-------|---------|
| `python` is not recognized | Re-run installer with "Add Python to PATH" checked, or add manually via System Properties → Environment Variables |
| `pip` is not recognized | Run `python -m ensurepip --upgrade` |
| `code` is not recognized | Re-run VS Code installer with "Add to PATH" checked |
| PowerShell: "running scripts is disabled" | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| OpenAI API returns `401` | Check your API key in `.env` — ensure no extra spaces or quotes |
| `faiss-cpu` install fails | Try `pip install faiss-cpu --no-cache-dir` or use `chromadb` as alternative |
| `chromadb` install fails on older Windows | Ensure Visual C++ Build Tools are installed: <https://visualstudio.microsoft.com/visual-cpp-build-tools/> |
| Virtual environment not activating | Use `.venv\Scripts\activate` (cmd) or `.venv\Scripts\Activate.ps1` (PowerShell) |
| Copilot not suggesting | Check license status at <https://github.com/settings/copilot> |
| Cursor/Windsurf not connecting | Ensure you are signed in and have an active subscription |
| Long path errors | Enable long paths: run as admin `reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f` and restart |

---

## Summary

After completing this guide, you should have:

- Python 3.11+ with pip
- Git configured
- VS Code with Python extensions
- One AI coding assistant installed and authenticated
- OpenAI API key verified and working
- All course Python packages installed in a virtual environment
- Jupyter notebooks running

**You are ready for Day 1!**
