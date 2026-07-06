
"""
DocuMind AI

Main FastAPI application.

This module creates and configures the FastAPI application.
"""

from fastapi import FastAPI

from backend.app.api.routers.health import router as health_router
from backend.app.api.routers.root import router as root_router
from backend.app.api.routers.chat import router as chat_router
from backend.app.api.routers.upload import router as upload_router



app = FastAPI(
    title="DocuMind AI",
    description="AI-powered document intelligence platform.",
    version="0.6.0"
)

app.include_router(root_router)
app.include_router(health_router)
app.include_router(chat_router)
app.include_router(upload_router)


