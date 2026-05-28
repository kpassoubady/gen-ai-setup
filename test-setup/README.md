# Setup Verification — Hello LLM

Run this self-contained project **before Day 1** to confirm your environment
works end to end: dependencies installed, credentials configured, and a real
response returned from the LLM.

A clean run prints `✅ SETUP VERIFIED` and you are ready for class.

---

## What is in here

| File | Purpose |
|:-----|:--------|
| `requirements.txt` | All Python packages used across the 4-day course |
| `.env.example` | Configuration template — copy to `.env` and fill in your values |
| `llm_client.py` | The same provider-agnostic client used in the course labs |
| `hello_llm.py` | Verification script: prints config, makes one live LLM call |

---

## Steps

### 1. Create and activate a virtual environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create your `.env`

macOS / Linux:

```bash
cp .env.example .env
```

Windows:

```cmd
copy .env.example .env
```

Open `.env` and fill in your values. Most teams use the **gateway** (no
personal API key required):

```
LLM_PROVIDER=azure
AZURE_API_BASE=https://<your-gateway-host>/<path>
AZURE_API_VERSION=2024-02-01
AZURE_DEPLOYMENT_DEFAULT=gpt-4o
AZURE_DEPLOYMENT_MINI=gpt-4o-mini
AZURE_AD_TOKEN=<your bearer token>
```

> The model/deployment name may change before class — just update
> `AZURE_DEPLOYMENT_DEFAULT` / `AZURE_DEPLOYMENT_MINI`. No code changes needed.
>
> If your gateway expects the standard Azure `api-key` header instead of a
> bearer token, set `AZURE_API_KEY` and leave `AZURE_AD_TOKEN` blank.

If you have a personal OpenAI / Gemini / Claude key instead, set
`LLM_PROVIDER` accordingly and fill in that key.

### 4. Run the verification

```bash
python3 hello_llm.py
```

(Windows: `python hello_llm.py`)

Expected output ends with:

```
✅ SETUP VERIFIED — you are ready for Day 1!
```

---

## Troubleshooting

| Symptom | Fix |
|:--------|:----|
| `AZURE_AD_TOKEN is NOT set` in config output | You did not create `.env` or left the token blank |
| `401` / `403` error | Token expired or wrong gateway URL — re-check `AZURE_API_BASE` and `AZURE_AD_TOKEN` |
| `404` / deployment not found | `AZURE_DEPLOYMENT_DEFAULT` does not match a deployment on the gateway |
| `ModuleNotFoundError` | Re-run `pip install -r requirements.txt` inside the activated venv |

If the call still fails after these checks, contact your instructor before the
training day.
