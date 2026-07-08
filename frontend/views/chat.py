"""
Chat Page

Allows users to chat with DocuMind AI.
"""

import streamlit as st

from services.api_client import ask_question

from components.document.selector import (
    render as render_document_selector,
)

from components.chat.history import (
    render as render_history,
)

from components.chat.input import (
    render as render_chat_input,
)

from components.chat.message import (
    render as render_message,
)


def render():
    """
    Render the Chat page.
    """

    # --------------------------------------------------
    # Session State
    # --------------------------------------------------

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # --------------------------------------------------
    # Header
    # --------------------------------------------------

    st.header("💬 Chat with DocuMind AI")

    st.write(
        "Ask questions about your indexed documents."
    )

    # --------------------------------------------------
    # Document Selector
    # --------------------------------------------------

    selected_document = render_document_selector()

    st.divider()

    # --------------------------------------------------
    # Chat History
    # --------------------------------------------------

    render_history(
        st.session_state.messages
    )

    # --------------------------------------------------
    # Chat Input
    # --------------------------------------------------

    question = render_chat_input()

    if not question:
        return

    # --------------------------------------------------
    # Save User Message
    # --------------------------------------------------

    user_message = {
        "role": "user",
        "content": question,
    }

    st.session_state.messages.append(
        user_message
    )

    render_message(
        role="user",
        content=question,
    )

    # --------------------------------------------------
    # Backend Request
    # --------------------------------------------------

    with st.spinner("Thinking..."):

        response = ask_question(
            question=question,
            document=selected_document,
        )

    if response.status_code != 200:

        st.error(
            "Failed to get a response."
        )

        return

    data = response.json()

    # --------------------------------------------------
    # Show Assistant Message
    # --------------------------------------------------

    render_message(
        role="assistant",
        content=data["answer"],
        sources=data["sources"],
    )

    assistant_message = {
        "role": "assistant",
        "content": data["answer"],
        "sources": data["sources"],
    }

    st.session_state.messages.append(
        assistant_message
    )