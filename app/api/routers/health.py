from fastapi import APIRouter
router = APIRouter()

@router.get("/live")
def live():
    return {"status": "alive"}

@router.get("/ready")
def ready():
    # in prod, check model bundle, external deps, etc.
    return {"status": "ready"}
