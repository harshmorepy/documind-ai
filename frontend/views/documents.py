"""
Documents View

Displays the indexed document library.
"""

import streamlit as st

from components.document.card import render as render_card
from components.document.empty_state import render as render_empty_state
from components.document.stats import render as render_stats
from services.api_client import list_documents


def render() -> None:
    """
    Render the Documents page.
    """

    st.title("📚 Document Library")
    st.caption(
        "Browse, manage, and explore your indexed knowledge base."
    )

    # ---------------------------------------------------------
    # Fetch documents
    # ---------------------------------------------------------

    try:
        response = list_documents()

    except Exception:
        st.error(
            "Unable to connect to the backend.\n\n"
            "Please make sure the FastAPI server is running."
        )
        return

    if response.status_code != 200:
        st.error("Failed to retrieve indexed documents.")
        return

    data = response.json()

    documents = data.get("documents", [])

    # ---------------------------------------------------------
    # Empty State
    # ---------------------------------------------------------

    if not documents:
        render_empty_state()
        return

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    total_documents = len(documents)
    total_chunks = sum(
        document.get("chunks", 0)
        for document in documents
    )

    render_stats(
        total_documents=total_documents,
        total_chunks=total_chunks,
    )

    # ---------------------------------------------------------
    # Document Cards
    # ---------------------------------------------------------

    for document in documents:

        render_card(
            display_name=document.get(
                "display_name",
                "Unknown Document",
            ),
            filename=document.get(
                "filename",
                "",
            ),
            chunks=document.get(
                "chunks",
                0,
            ),
        )