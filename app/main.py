from fastapi import FastAPI

from app.schemas import EmiRequest, EmiResponse, SipRequest, SipResponse
from app.services import calculate_emi, calculate_sip

app = FastAPI(title="Finance Calculator API", version="1.0.0")


@app.post("/emi", response_model=EmiResponse, response_model_exclude_none=True)
def emi(req: EmiRequest):
    return calculate_emi(req)


@app.post("/sip", response_model=SipResponse)
def sip(req: SipRequest):
    return calculate_sip(req)
