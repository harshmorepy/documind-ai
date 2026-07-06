"""
PDF Service

This module contains the business logic for handling PDF uploads.
"""

from pathlib import Path
import shutil

from fastapi import HTTPException, UploadFile, status
from backend.app.indexer import index_pdf


class PDFService:
    def validate_pdf(self, uploaded_file: UploadFile) -> None:
        """
        Validate the uploaded PDF file.

        Raises
            HTTPException: If the uploaded file is invalid.
        """

        if uploaded_file.filename is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No filename provided."
            )

        if not uploaded_file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only PDF files are allowed."
            )
            
            
            
    def save_pdf(self, uploaded_file: UploadFile) -> Path:
        """
        Save an uploaded PDF to the upload directory.

        Returns:
            Path: Path to the saved PDF.
        """

        destination = self.upload_directory / uploaded_file.filename

        try:
            with destination.open("wb") as buffer:
                shutil.copyfileobj(uploaded_file.file, buffer)

            return destination

        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to save PDF: {error}"
            )
            
            
            
            
    def index_uploaded_pdf(self, pdf_path: Path) -> dict:
        """
        Index a saved PDF into the vector database.

        Args:
            pdf_path: Path to the saved PDF.

        Returns:
            Dictionary containing indexing results.
        """

        return index_pdf(pdf_path)
        

    

    """
    Handles all PDF-related operations.

    Responsibilities:
    - Validate uploaded PDFs
    - Save uploaded files
    - Trigger automatic indexing
    """

    def __init__(self):
        self.upload_directory = Path("data/pdfs")
        self.upload_directory.mkdir(parents=True, exist_ok=True)