"""
Chat API

Provides endpoints for interacting with DocuMind AI.
"""

from fastapi import APIRouter

from backend.app.schemas.chat import (
    ChatRequest,
    ChatResponse
)
from backend.app.services.rag_service import ask_question

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "/",
    response_model=ChatResponse
)
def chat(request: ChatRequest):
    """
    Ask DocuMind AI a question.
    """

    result = ask_question(
        question=request.question,
        document=request.document,
    )
    
    
    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"]
    )