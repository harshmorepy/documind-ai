"""
API Client

Centralized communication with the DocuMind AI backend.

All frontend requests should pass through this module.
"""

import requests


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

BASE_URL = "http://127.0.0.1:8000"


# ---------------------------------------------------------------------
# Upload API
# ---------------------------------------------------------------------

def upload_pdf(file):
    """
    Upload a PDF to DocuMind AI.

    Args:
        file: Uploaded PDF file.

    Returns:
        requests.Response
    """

    files = {
        "file": (
            file.name,
            file,
            "application/pdf",
        )
    }

    response = requests.post(
        f"{BASE_URL}/upload/",
        files=files,
    )

    return response



# ---------------------------------------------------------------------
# Documents API
# ---------------------------------------------------------------------

def list_documents():
    """
    Retrieve all indexed documents.

    Returns:
        requests.Response
    """

    response = requests.get(
        f"{BASE_URL}/documents/"
    )

    return response



def ask_question(
    question: str,
    document: str | None = None,
):
    """
    Send a question to the Chat API.
    """

    payload = {
    "question": question,
}

    if document:
        payload["document"] = document

    response = requests.post(
        f"{BASE_URL}/chat/",
        json=payload,
    )

    return response