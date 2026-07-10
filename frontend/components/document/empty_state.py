"""
Empty State Component

Displays a friendly empty state when no indexed
documents are available in the knowledge base.
"""

import streamlit as st


def render() -> None:
    """
    Render the empty document library state.
    """

    st.markdown("## 📂")
    st.subheader("Your Document Library is Empty")

    st.write(
        """
        Upload your first PDF to begin building your AI knowledge base.

        Once indexed, your documents will appear here and will be
        available for semantic search and AI-powered conversations.
        """
    )

    st.button(
        "📤 Upload Your First Document",
        disabled=True,
        use_container_width=True,
    )

    st.caption(
        "Go to the **Upload** page from the sidebar to add a document."
    )