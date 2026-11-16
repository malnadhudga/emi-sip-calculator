from typing import List, Optional

from pydantic import BaseModel, Field


class EmiRequest(BaseModel):
    principal: float = Field(..., gt=0, description="Loan amount")
    annual_rate: float = Field(..., ge=0, le=50, description="Interest rate % per year")
    tenure_months: int = Field(..., gt=0, le=600)
    include_schedule: bool = False


class ScheduleRow(BaseModel):
    month: int
    emi: float
    principal_paid: float
    interest_paid: float
    balance: float


class EmiResponse(BaseModel):
    emi: float
    total_payment: float
    total_interest: float
    schedule: Optional[List[ScheduleRow]] = None


class SipRequest(BaseModel):
    monthly_investment: float = Field(..., gt=0)
    expected_return: float = Field(..., ge=0, le=50, description="Expected return % per year")
    years: int = Field(..., gt=0, le=50)


class SipResponse(BaseModel):
    invested_amount: float
    estimated_returns: float
    maturity_value: float
