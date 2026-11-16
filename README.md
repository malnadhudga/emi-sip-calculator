# EMI & SIP Calculator API

A small FastAPI service that calculates loan EMIs and SIP maturity values.
See [docs/PROJECT_OVERVIEW.md](docs/PROJECT_OVERVIEW.md) for what the project does and what each endpoint returns.

## Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/malnadhudga/emi-sip-calculator.git
cd emi-sip-calculator
```

### 2. Create and activate a virtual environment

Create the venv:

```bash
python -m venv venv
```

Activate it (pick your terminal):

**Windows – PowerShell**
```powershell
venv\Scripts\Activate.ps1
```
> If PowerShell says running scripts is disabled, run this once, then activate again:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

**Windows – Command Prompt (cmd)**
```cmd
venv\Scripts\activate.bat
```

**macOS / Linux**
```bash
source venv/bin/activate
```

When it's active you'll see `(venv)` at the start of your terminal prompt. To leave it later, run `deactivate`.

### 3. Install the requirements

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run the server

```bash
python -m uvicorn app.main:app --reload
```

Open the interactive docs at http://127.0.0.1:8000/docs
