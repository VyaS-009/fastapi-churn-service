from pydantic import BaseModel, Field

class ChurnRequest(BaseModel):
    tenure: float = Field(ge=0)
    MonthlyCharges: float = Field(ge=0)
    TotalCharges: float = Field(ge=0)
    Contract: str
    InternetService: str
    OnlineSecurity: str
    TechSupport: str
    PaymentMethod: str

class ChurnResponse(BaseModel):
    churn_prediction: int
    confidence: float | None = None
