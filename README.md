# EMI & SIP Calculator API

A small FastAPI service that calculates loan EMIs and SIP maturity values.
You send numbers as JSON, it validates them and returns the calculated result.

## Project structure

```text
emi-sip-calculator/
├── main.py            # FastAPI app, request/response models and routes
├── functions.py       # the EMI and SIP formulas
└── requirements.txt
```

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
python -m uvicorn main:app --reload
```

Open the interactive docs at http://127.0.0.1:8000/docs

## Endpoints

### `POST /emi` — Loan EMI calculator

Works out the fixed monthly instalment (EMI) for a loan, plus the total amount paid and total interest.

| Field | Type | Rules | Meaning |
|---|---|---|---|
| `principal` | number | > 0 | Loan amount |
| `annual_rate` | number | 0 – 50 | Interest rate, % per year |
| `tenure_months` | integer | 1 – 600 | Loan length in months |
| `include_schedule` | boolean | optional, default `false` | Also return a month-by-month repayment table |

```json
// request
{"principal": 500000, "annual_rate": 9, "tenure_months": 60}

// response
{"emi": 10379.18, "total_payment": 622750.66, "total_interest": 122750.66}
```

### `POST /sip` — SIP maturity calculator

Estimates what a monthly investment (SIP) grows to after a number of years at an expected annual return.

| Field | Type | Rules | Meaning |
|---|---|---|---|
| `monthly_investment` | number | > 0 | Amount invested each month |
| `expected_return` | number | 0 – 50 | Expected return, % per year |
| `years` | integer | 1 – 50 | Investment period in years |

```json
// request
{"monthly_investment": 5000, "expected_return": 12, "years": 10}

// response
{"invested_amount": 600000, "estimated_returns": 561695.38, "maturity_value": 1161695.38}
```

Invalid input (for example a negative `principal`) is rejected with HTTP **422** and a message naming the bad field.
