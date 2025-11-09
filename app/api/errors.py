from fastapi import Request, status
from fastapi.responses import JSONResponse
import logging

async def unhandled_exceptions(request: Request, exc: Exception):
    logging.exception("Unhandled error", exc_info=exc)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"}
    )
