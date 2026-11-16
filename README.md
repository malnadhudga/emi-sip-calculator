# EMI & SIP Calculator API

A small FastAPI service that calculates loan EMIs and SIP maturity values.
See [docs/PROJECT_OVERVIEW.md](docs/PROJECT_OVERVIEW.md) for what the project does and what each endpoint returns.

> **Python version:** requires Python **3.8 – 3.10**. Installing on Python 3.11+ fails on purpose (`requires-python = ">=3.8,<3.11"` in `pyproject.toml`).

## Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/malnadhudga/emi-sip-calculator.git
cd emi-sip-calculator
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

- Windows (PowerShell): `venv\Scripts\Activate.ps1`
- Windows (cmd): `venv\Scripts\activate.bat`
- macOS / Linux: `source venv/bin/activate`

### 3. Install the requirements

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

Open the interactive docs at http://127.0.0.1:8000/docs
