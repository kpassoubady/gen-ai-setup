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

## 6. OpenAI API Key Setup

1. Go to <https://platform.openai.com/api-keys> and create a new API key.
2. Ensure your account has at least **$5 credit** for lab exercises.
3. Store the key securely — never commit it to source control.

Create a `.env` file in your project directory:

```bash
echo 'OPENAI_API_KEY=sk-your-key-here' > .env
```

Verify the key works:

```bash
python3 -c "
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
r = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[{'role':'user','content':'Say hello in one word'}],
    max_tokens=10
)
print('API connection successful:', r.choices[0].message.content)
"
```

---

## 7. Install Python Packages

Create and activate a virtual environment:

```bash
mkdir -p ~/gen-ai-course && cd ~/gen-ai-course
python3 -m venv .venv
source .venv/bin/activate
```

Create `requirements.txt`:

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

```bash
pip3 install -r requirements.txt
```

Verify key packages:

```bash
python3 -c "import openai; print('openai', openai.__version__)"
python3 -c "import tiktoken; print('tiktoken OK')"
python3 -c "import faiss; print('faiss OK')"
python3 -c "import chromadb; print('chromadb OK')"
python3 -c "import flask; print('flask', flask.__version__)"
python3 -c "import fastapi; print('fastapi OK')"
python3 -c "import numpy; print('numpy', numpy.__version__)"
```

---

## 8. Clone the Course Repository

Your instructor will provide the repository URL. Clone it:

```bash
git clone <REPO_URL> ~/gen-ai-course/repo
cd ~/gen-ai-course/repo
```

Copy your `.env` file into the repo root:

```bash
cp ~/gen-ai-course/.env ~/gen-ai-course/repo/.env
```

---

## 9. Jupyter Notebook Verification

```bash
cd ~/gen-ai-course
source .venv/bin/activate
jupyter notebook --no-browser
```

Open the URL shown in the terminal. Create a new Python 3 notebook and run:

```python
import openai, tiktoken, numpy
print("All imports successful — you are ready for class!")
```

---

## 10. Troubleshooting

| Issue | Solution |
|-------|---------|
| `python3: command not found` | Run `brew install python` and restart terminal |
| `pip3: command not found` | Run `python3 -m ensurepip --upgrade` |
| `code: command not found` | Open VS Code → `Cmd+Shift+P` → "Shell Command: Install 'code' command in PATH" |
| OpenAI API returns `401` | Check your API key in `.env` — ensure no extra spaces or quotes |
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
- OpenAI API key verified and working
- All course Python packages installed in a virtual environment
- Jupyter notebooks running

**You are ready for Day 1!**
