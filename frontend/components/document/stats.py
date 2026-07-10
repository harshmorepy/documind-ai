"""
Document Statistics Component

Displays a high-level overview of the indexed
knowledge base.
"""

import streamlit as st


def render(
    total_documents: int,
    total_chunks: int,
) -> None:
    """
    Render document library statistics.

    Args:
        total_documents: Total indexed documents.
        total_chunks: Total indexed chunks.
    """

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="📄 Documents",
            value=total_documents,
        )

    with col2:
        st.metric(
            label="📦 Chunks",
            value=total_chunks,
        )

    with col3:
        st.metric(
            label="🟢 Status",
            value="Ready",
        )

    st.divider()