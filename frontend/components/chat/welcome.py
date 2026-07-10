"""
Welcome Component

Displayed when the chat history is empty.
"""

import streamlit as st


def render():
    """
    Render the welcome screen.
    """

    st.markdown("## 👋 Welcome to DocuMind AI")

    st.write(
        "Your AI-powered document intelligence platform."
    )

    st.divider()

    st.markdown("### 💡 Try asking")

    col1, col2 = st.columns(2)

    with col1:
        st.info("Explain recursion.")
        st.info("Summarize this document.")
        st.info("Generate interview questions.")

    with col2:
        st.info("Compare classes and objects.")
        st.info("Explain decorators.")
        st.info("What are Python generators?")

    st.divider()

    st.caption(
        "📂 Select a document above or search across all indexed documents."
    )