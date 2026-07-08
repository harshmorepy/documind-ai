"""
Chat Input Component
"""

import streamlit as st


def render():
    """
    Render the chat input.

    Returns:
        str | None
    """

    return st.chat_input(
        "Ask DocuMind AI..."
    )