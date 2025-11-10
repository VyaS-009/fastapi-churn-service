from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_prometheus import PrometheusMiddleware, metrics
from app.core.config import settings
from app.core.logging import setup_logging
from app.api.routers import health, predict
from app.api.errors import unhandled_exceptions

def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(title=settings.APP_NAME)

    # PrometheusMiddleware should be the first middleware to be added
    if settings.ENABLE_METRICS:
        # This middleware will also log request timing
        app.add_middleware(PrometheusMiddleware)
        app.add_route("/metrics", metrics)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(health.router, prefix=f"{settings.API_V1_PREFIX}/health", tags=["Health"])
    app.include_router(predict.router, prefix=f"{settings.API_V1_PREFIX}", tags=["Prediction"])
    app.add_exception_handler(Exception, unhandled_exceptions)
    return app

app = create_app()
