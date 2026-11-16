# Project Overview

**EMI & SIP Calculator API** is a FastAPI service with two personal-finance calculators.
You send numbers as JSON, it validates them and returns the calculated result.

## Endpoints

### `POST /emi` — Loan EMI calculator

Works out the fixed monthly instalment (EMI) for a loan, plus the total amount paid and total interest.

| Field | Type | Rules | Meaning |
|---|---|---|---|
| `principal` | number | > 0 | Loan amount |
| `annual_rate` | number | 0 – 50 | Interest rate, % per year |
| `tenure_months` | integer | 1 – 600 | Loan length in months |
| `include_schedule` | boolean | optional, default `false` | Also return a month-by-month repayment table |

Example:

```json
// request
{"principal": 500000, "annual_rate": 9, "tenure_months": 60}

// response
{"emi": 10379.18, "total_payment": 622750.66, "total_interest": 122750.66}
```

With `include_schedule: true`, the response also has a `schedule` list showing, for each month, the EMI, principal paid, interest paid and remaining balance.

### `POST /sip` — SIP maturity calculator

Estimates what a monthly investment (SIP) grows to after a number of years at an expected annual return.

| Field | Type | Rules | Meaning |
|---|---|---|---|
| `monthly_investment` | number | > 0 | Amount invested each month |
| `expected_return` | number | 0 – 50 | Expected return, % per year |
| `years` | integer | 1 – 50 | Investment period in years |

Example:

```json
// request
{"monthly_investment": 5000, "expected_return": 12, "years": 10}

// response
{"invested_amount": 600000, "estimated_returns": 561695.38, "maturity_value": 1161695.38}
```

## Validation

Invalid input (for example a negative `principal`) is rejected with HTTP **422** and a message naming the bad field.

## Project structure

- `app/main.py` — routes
- `app/schemas.py` — request/response models and validation rules
- `app/services.py` — the EMI and SIP formulas
