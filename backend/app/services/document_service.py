"""
Document Service

Provides operations related to indexed documents.
"""

from collections import Counter

from backend.app.vector_store import collection
from backend.app.schemas.document import (
    DocumentInfo,
    DocumentListResponse,
)

class DocumentService:
    """
    Handles document management operations.
    """
    def list_documents(self) -> DocumentListResponse:
        """
        Return all indexed documents.
        """
        results = self.collection.get(include=["metadatas"])

        metadata_list = results.get("metadatas", [])

        document_counter = Counter()

        for metadata in metadata_list:
            if metadata and "pdf_name" in metadata:
                document_counter[metadata["pdf_name"]] += 1

        documents = []
            
        for filename, chunks in sorted(document_counter.items()):
            display_name = (
                filename
                .replace("_", " ")
                .title()
            )
            
            documents.append(
                DocumentInfo(
                    filename=filename,
                    display_name=display_name,
                    chunks=chunks,
                )
            )

            

        return DocumentListResponse(documents=documents)
    
    def __init__(self):
        self.collection = collection