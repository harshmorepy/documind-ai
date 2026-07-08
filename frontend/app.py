"""
DocuMind AI

Frontend Entry Point
"""

import streamlit as st

from components.sidebar import render_sidebar
from views import chat
from views import documents
from views import upload


st.set_page_config(
    page_title="DocuMind AI",
    page_icon="📚",
    layout="wide",
)

page = render_sidebar()

st.title("🤖 DocuMind AI")

st.caption(
    "AI-powered document intelligence platform."
)

st.divider()

if page == "Upload":
    upload.render()

elif page == "Chat":
    chat.render()

elif page == "Documents":
    documents.render()