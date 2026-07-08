"""
Document Selector Component

Provides a reusable document selector for DocuMind AI.
"""

import streamlit as st

from services.api_client import list_documents


def render():
    """
    Render the document selector.

    Returns:
        str | None:
            Selected document filename, or None if
            "All Documents" is selected.
    """

    response = list_documents()

    document_names = []

    if response.status_code == 200:

        documents = response.json()["documents"]

        document_names = [
            document["filename"]
            for document in documents
        ]

    selected_document = st.selectbox(
        "📂 Search Scope",
        options=["All Documents"] + document_names,
    )

    if selected_document == "All Documents":
        return None

    return selected_document