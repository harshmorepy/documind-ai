"""
Sidebar Component

Provides navigation for the DocuMind AI frontend.
"""

import streamlit as st


def render_sidebar():
    """
    Render the application sidebar.

    Returns:
        Selected page name.
    """

    st.sidebar.title("📚 DocuMind AI")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Upload",
            "Chat",
            "Documents",
        ],
    )

    st.sidebar.divider()

    st.sidebar.caption("Version v0.9.0")

    return page