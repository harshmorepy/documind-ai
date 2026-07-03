"""
Health API

Provides endpoints to verify that the backend is running.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():
    """
    Health check endpoint.
    """

    return {
        "status": "healthy",
        "application": "DocuMind AI",
        "version": "0.6.0"
    }