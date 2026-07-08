"""
Upload Page

Allows users to upload and index PDF documents.
"""

import streamlit as st

from services.api_client import upload_pdf


def render():
    """
    Render the Upload page.
    """

    st.header("📄 Upload PDF")

    st.write(
        "Upload a PDF to index it into DocuMind AI."
    )

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"],
    )

    if uploaded_file is None:
        return

    st.success(
        f"Selected: {uploaded_file.name}"
    )

    if st.button(
        "🚀 Upload",
        use_container_width=True,
    ):

        with st.spinner("Uploading document..."):

            response = upload_pdf(uploaded_file)

        if response.status_code == 200:
            data = response.json()

            st.success("✅ Document indexed successfully!")

            st.markdown("### 📄 File")
            st.write(data["filename"])

            st.metric(
                label="🧩 Chunks Indexed",
                value=data["chunks"],
            )

            st.success("🎉 Ready for Chat!")

        else:

            st.error("❌ Upload failed.")

            try:
                st.json(response.json())

            except Exception:
                st.text(response.text)