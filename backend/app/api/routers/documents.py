"""
Document API Router

Provides endpoints for managing indexed documents.
"""

from fastapi import APIRouter

from backend.app.schemas.document import DocumentListResponse
from backend.app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

document_service = DocumentService()


@router.get("/", response_model=DocumentListResponse)
async def list_documents():
    """
    List all indexed documents.
    """
    return document_service.list_documents()