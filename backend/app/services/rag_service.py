"""
RAG Service

Contains the business logic for answering
questions using the RAG pipeline.
"""

from backend.app.rag import answer_question


def ask_question(question: str):
    """
    Ask DocuMind AI a question.

    Returns a JSON-ready dictionary.
    """

    result = answer_question(question)

    sources = []

    if result["sources"]:

        sources = [
            source.strip()
            for source in result["sources"].split("\n")
            if source.strip()
        ]

    return {
        "answer": result["answer"],
        "sources": sources
    }