"""
Document Card Component

Renders a single indexed document as a clean,
reusable card.
"""

import streamlit as st


def render(
    display_name: str,
    filename: str,
    chunks: int,
) -> None:
    """
    Render a document card.

    Args:
        display_name: Human-readable document name.
        filename: Internal normalized filename.
        chunks: Total indexed chunks.
    """

    with st.container(border=True):

        st.subheader(f"📄 {display_name}")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(
                f"""
                <span style="
                    color:#22c55e;
                    font-weight:600;
                    font-size:0.95rem;
                ">
                🟢 Ready for Chat
                </span>
                """,
                unsafe_allow_html=True,
            )

            st.caption(f"📦 {chunks} Chunks Indexed")

            st.caption(f"🆔 {filename}")

        with col2:
            st.metric(
                label="📦 Chunks",
                value=chunks,
            )

        st.divider()

        if st.button(
            "💬 Open in Chat",
            key=f"chat_{filename}",
            use_container_width=True,
        ):
            st.session_state["selected_document"] = filename

            st.success(
                f'"{display_name}" is ready for chat.\n\n'
                "Open the Chat page to begin asking questions."
            )