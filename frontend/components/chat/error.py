"""
Chat Error Component

Displays user-friendly error messages for
common chat failures.
"""

import streamlit as st


def backend_unavailable() -> None:
    """
    Display a backend connection error.
    """

    st.error(
        """
        ### 🔌 Unable to connect to DocuMind AI

        Please make sure the FastAPI backend is running,
        then try your request again.
        """
    )


def ai_service_unavailable() -> None:
    """
    Display an AI service error.
    """

    st.error(
        """
        ### 🤖 AI Service Unavailable

        DocuMind AI couldn't generate a response right now.

        Please try again in a few moments.
        """
    )


def no_results() -> None:
    """
    Display a no-results message.
    """

    st.info(
        """
        ### 📄 No Relevant Information Found

        I couldn't find information related to your question.

        Try:

        - Asking a more specific question
        - Selecting another document
        - Uploading additional documents
        """
    )


def unexpected_error() -> None:
    """
    Display an unexpected error.
    """

    st.error(
        """
        ### ⚠️ Something Went Wrong

        An unexpected error occurred.

        Please try again.
        """
    )