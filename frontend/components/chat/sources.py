"""
Sources Component
"""

import streamlit as st


def render(sources):
    """
    Render retrieved sources.
    """

    if not sources:
        return

    with st.expander("📚 Sources"):

        for source in sources:

            st.write(f"• {source}")