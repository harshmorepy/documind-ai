"""
Root API

Provides the root endpoint for DocuMind AI.
"""

from fastapi import APIRouter

router = APIRouter(tags=["Root"])


@router.get("/")
def root():
    """
    Root endpoint.
    """

    return {
        "application": "DocuMind AI",
        "version": "0.6.0",
        "status": "running"
    }