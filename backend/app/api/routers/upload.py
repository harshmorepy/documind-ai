"""
Upload API router.

This module provides endpoints for uploading PDF documents.
"""

from fastapi import APIRouter,  File, UploadFile

from backend.app.schemas.upload import UploadResponse
from backend.app.services.pdf_service import PDFService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

pdf_service = PDFService()


@router.post("/", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload, validate, save and index a PDF.
    """

    pdf_service.validate_pdf(file)

    saved_file = pdf_service.save_pdf(file)

    indexing_result = pdf_service.index_uploaded_pdf(saved_file)

    return UploadResponse(
        status=indexing_result["status"],
        filename=indexing_result["pdf_name"],
        chunks=indexing_result["total_chunks"],
    )