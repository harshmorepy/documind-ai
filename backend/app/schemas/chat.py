"""
Chat API Schemas

Defines request and response models
for the chat endpoint.
"""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Request model for asking DocuMind AI a question.
    """

    question: str = Field(
        examples=["What is FastAPI?"],
        description="The question to ask DocuMind AI."
    )
    document: str | None = Field(
        default=None,
        examples=["python_notes"],
        description=(
            "Optional. Specify a document name returned by GET /documents. " 
            "If omitted. DocuMind AI will search across all indexed documents."
        ),
    )


class ChatResponse(BaseModel):
    """
    Chat response model.
    """

    answer: str
    sources: list[str]