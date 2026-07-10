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

    try:
        response = list_documents()

    except Exception:
        st.warning(
            "🔌 Unable to load indexed documents.\n\n"
            "Please make sure the backend server is running."
        )
        return None

    document_names = []

    if response.status_code == 200:

        documents = response.json()["documents"]

        document_names = [
            document["filename"]
            for document in documents
        ]

    else:
        st.warning(
            "Unable to retrieve the document list."
        )
        return None

    options = ["All Documents"] + document_names

    default_index = 0

    saved_document = st.session_state.get("selected_document")

    if (
        saved_document
        and saved_document in options
    ):
        default_index = options.index(saved_document)

    selected_document = st.selectbox(
        "📂 Search Scope",
        options=options,
        index=default_index,
    )

    # Clear the one-time selection
    st.session_state.pop(
        "selected_document",
        None,
    )

    if selected_document == "All Documents":
        return None

    return selected_document