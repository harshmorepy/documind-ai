"""
Chat API Schemas

Defines request and response models
for the chat endpoint.
"""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Chat request model.
    """

    question: str


class ChatResponse(BaseModel):
    """
    Chat response model.
    """

    answer: str
    sources: list[str]