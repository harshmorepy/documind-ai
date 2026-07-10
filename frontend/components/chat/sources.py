"""
Sources Component

Displays retrieved document sources used to
generate the AI response.
"""

import re
from collections import defaultdict

import streamlit as st


def _group_consecutive(numbers: list[int]) -> list[str]:
    """
    Convert a list of chunk numbers into ranges.

    Example:
        [33,34,35,36,60,61,62,73]

    Returns:
        ["33–36", "60–62", "73"]
    """

    if not numbers:
        return []

    numbers = sorted(set(numbers))

    ranges = []

    start = prev = numbers[0]

    for number in numbers[1:]:

        if number == prev + 1:
            prev = number
            continue

        if start == prev:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}–{prev}")

        start = prev = number

    if start == prev:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}–{prev}")

    return ranges


def render(sources):
    """
    Render grouped document sources.
    """

    if not sources:
        return

    grouped_sources = defaultdict(list)

    for source in sources:

        match = re.match(
            r"(.+?)\s+\(Chunk\s+(\d+)\)",
            source,
        )

        if match:

            filename = match.group(1)

            chunk = int(match.group(2))

            grouped_sources[filename].append(chunk)

        else:

            grouped_sources[source]

    with st.expander(
        f"📚 Sources Used ({len(sources)})",
        expanded=False,
    ):

        for filename, chunks in grouped_sources.items():

            with st.container(border=True):

                display_name = (
                    filename
                    .replace("_", " ")
                    .title()
                )

                st.markdown(
                    f"### 📄 {display_name}"
                )

                if chunks:

                    ranges = _group_consecutive(
                        chunks
                    )

                    st.caption(
                        "📦 Chunks Used"
                    )

                    st.write(
                        ", ".join(ranges)
                    )

                    st.divider()

                    st.success(
                        f"{len(chunks)} chunk(s) contributed to this answer."
                    )

                else:

                    st.info(
                        "Source metadata unavailable."
                    )