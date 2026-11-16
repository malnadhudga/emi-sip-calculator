# ---------- EMI ----------

def calculate_emi(principal, annual_rate, tenure_months, include_schedule=False):
    monthly_rate = annual_rate / 12 / 100
    n = tenure_months

    if monthly_rate == 0:
        emi = principal / n
    else:
        factor = (1 + monthly_rate) ** n
        emi = principal * monthly_rate * factor / (factor - 1)

    total_payment = emi * n

    result = {
        "emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_payment - principal, 2),
    }

    if include_schedule:
        result["schedule"] = build_schedule(principal=principal, monthly_rate=monthly_rate, emi=emi, n=n)

    return result


def build_schedule(principal, monthly_rate, emi, n):
    rows = []
    balance = principal

    for month in range(1, n + 1):
        interest = balance * monthly_rate
        principal_paid = emi - interest
        balance = max(balance - principal_paid, 0)
        rows.append({
            "month": month,
            "emi": round(emi, 2),
            "principal_paid": round(principal_paid, 2),
            "interest_paid": round(interest, 2),
            "balance": round(balance, 2),
        })

    return rows


# ---------- SIP ----------

def calculate_sip(monthly_investment, expected_return, years):
    monthly_rate = expected_return / 12 / 100
    months = years * 12
    invested = monthly_investment * months

    if monthly_rate == 0:
        maturity = invested
    else:
        maturity = monthly_investment * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)

    return {
        "invested_amount": round(invested, 2),
        "estimated_returns": round(maturity - invested, 2),
        "maturity_value": round(maturity, 2),
    }
