"""
Chat History Component
"""

from components.chat.message import render as render_message


def render(messages):
    """
    Render all chat messages.
    """

    for message in messages:

        render_message(
            role=message["role"],
            content=message["content"],
            sources=message.get("sources"),
        )