from fastapi import APIRouter, Depends
from app.schemas.churn import ChurnRequest, ChurnResponse
from app.api.deps import secure
from app.infra.model_loader import load_bundle
from app.infra.preprocessing import preprocess_single
import numpy as np

router = APIRouter()

@router.post("/predict", response_model=ChurnResponse)
def predict(req: ChurnRequest, _: bool = Depends(secure)):
    bundle = load_bundle()
    X = preprocess_single(req.model_dump(), bundle.x_columns, bundle.scaler)
    pred = bundle.model.predict(X)[0]
    proba = 0.0
    if hasattr(bundle.model, "predict_proba"):
        proba = float(np.max(bundle.model.predict_proba(X)))
    return ChurnResponse(churn_prediction=int(pred), confidence=proba)
