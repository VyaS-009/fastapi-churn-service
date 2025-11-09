import joblib, logging
from app.infra.model_registry import model_paths

class ModelBundle:
    def __init__(self, model, scaler, x_columns):
        self.model = model
        self.scaler = scaler
        self.x_columns = x_columns

_bundle: ModelBundle | None = None

def load_bundle() -> ModelBundle:
    global _bundle
    if _bundle:
        return _bundle
    p = model_paths()
    model = joblib.load(p["model"])
    scaler = joblib.load(p["scaler"])
    x_columns = joblib.load(p["xcolumns"])
    logging.getLogger(__name__).info("Model bundle loaded.")
    _bundle = ModelBundle(model, scaler, x_columns)
    return _bundle
