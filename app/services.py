from typing import List

from app.schemas import EmiRequest, EmiResponse, ScheduleRow, SipRequest, SipResponse


def calculate_emi(req: EmiRequest) -> EmiResponse:
    monthly_rate = req.annual_rate / 12 / 100
    n = req.tenure_months

    if monthly_rate == 0:
        emi = req.principal / n
    else:
        factor = (1 + monthly_rate) ** n
        emi = req.principal * monthly_rate * factor / (factor - 1)

    total_payment = emi * n
    schedule = _build_schedule(req.principal, monthly_rate, emi, n) if req.include_schedule else None

    return EmiResponse(
        emi=round(emi, 2),
        total_payment=round(total_payment, 2),
        total_interest=round(total_payment - req.principal, 2),
        schedule=schedule,
    )


def _build_schedule(principal: float, monthly_rate: float, emi: float, n: int) -> List[ScheduleRow]:
    rows, balance = [], principal
    for month in range(1, n + 1):
        interest = balance * monthly_rate
        principal_paid = emi - interest
        balance = max(balance - principal_paid, 0)
        rows.append(ScheduleRow(
            month=month,
            emi=round(emi, 2),
            principal_paid=round(principal_paid, 2),
            interest_paid=round(interest, 2),
            balance=round(balance, 2),
        ))
    return rows


def calculate_sip(req: SipRequest) -> SipResponse:
    monthly_rate = req.expected_return / 12 / 100
    months = req.years * 12
    invested = req.monthly_investment * months

    if monthly_rate == 0:
        maturity = invested
    else:
        maturity = req.monthly_investment * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)

    return SipResponse(
        invested_amount=round(invested, 2),
        estimated_returns=round(maturity - invested, 2),
        maturity_value=round(maturity, 2),
    )
