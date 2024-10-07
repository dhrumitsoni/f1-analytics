from typing import Any
from fastapi.responses import JSONResponse
from app.schemas.response import StandardResponse


def success_response(data: Any = None, message: str = "Request successful"):
    return JSONResponse(
        content=StandardResponse(
            status="success",
            message=message,
            data=data
        ).dict()
    )


def error_response(message: str = "An error occurred", data: Any = None, status_code: int = 400):
    """Generate a standard error response."""
    return JSONResponse(
        content=StandardResponse(
            status="error",
            message=message,
            data=data
        ).dict(),
        status_code=status_code
    )
