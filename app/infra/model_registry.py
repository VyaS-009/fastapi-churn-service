from pathlib import Path
from app.core.config import settings

def model_paths():
    base = Path(settings.MODEL_DIR)
    return {
        "model": base / settings.MODEL_FILE,
        "scaler": base / settings.SCALER_FILE,
        "xcolumns": base / settings.XCOLUMNS_FILE,
    }
