"""
Document schemas.

These schemas represent uploaded documents.
"""

from pydantic import BaseModel


class DocumentInfo(BaseModel):
    """
    Basic information about an indexed document.
    """

    filename: str
    display_name: str | None = None
    chunks: int
    

class DocumentListResponse(BaseModel):
    """
    Response returned when listing documents.
    """

    documents: list[DocumentInfo]