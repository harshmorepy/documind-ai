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

    USER_AVATAR = "🧸"
    ASSISTANT_AVATAR = "🟢"

    avatar = USER_AVATAR if role == "user" else ASSISTANT_AVATAR

    with st.chat_message(role, avatar=avatar):
        

        st.markdown(content)

        if role == "assistant":

            render_sources(sources)