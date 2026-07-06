"""
Schemas for PDF upload endpoints.
"""

from pydantic import BaseModel


class UploadResponse(BaseModel):
    """
    Response returned after a successful PDF upload.
    """

    status: str
    filename: str
    chunks: int