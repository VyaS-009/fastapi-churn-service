from fastapi import Depends
from app.core.security import require_api_key

def secure(dep=Depends(require_api_key)):
    return True
