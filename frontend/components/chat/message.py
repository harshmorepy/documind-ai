"""
Message Component
"""

import streamlit as st

from components.chat.sources import render as render_sources


def render(
    role,
    content,
    sources=None,
):
    """
    Render a chat message.
    """

    with st.chat_message(role):

        st.markdown(content)

        if role == "assistant":

            render_sources(sources)