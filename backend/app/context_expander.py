"""
Context Expansion Module

This module is responsible for improving the quality of retrieved
document context before it is sent to the LLM.

Current Version:
- Orders retrieved chunks.
- Removes duplicate chunks.

Future Versions:
- Context expansion (previous/next chunks)
- Multi-document support
- Adaptive context windows
"""
from backend.app.vector_store import get_chunk_by_number
from backend.app.core.constants import CONTEXT_WINDOW


def expand_chunks_v1(documents, metadatas):
    """
    Expand each retrieved chunk by including
    the previous and next chunk.
    """

    combined = []

    for document, metadata in zip(documents, metadatas):

        pdf_name = metadata["pdf_name"]
        chunk_number = metadata["chunk_number"]

        previous_chunk = get_chunk_by_number(
            pdf_name,
            chunk_number - 1
        )

        if previous_chunk:
            combined.append(previous_chunk)

        combined.append({
            "document": document,
            "metadata": metadata
        })

        next_chunk = get_chunk_by_number(
            pdf_name,
            chunk_number + 1
        )

        if next_chunk:
            combined.append(next_chunk)

    return combined



def remove_duplicates(chunks):
    """
    Remove duplicate chunks while preserving order.
    """

    unique_chunks = []
    seen = set()

    for item in chunks:

        chunk_id = (
            item["metadata"]["pdf_name"],
            item["metadata"]["chunk_number"]
        )

        if chunk_id not in seen:
            seen.add(chunk_id)
            unique_chunks.append(item)

    return unique_chunks



def extract_results(chunks):
    """
    Split expanded chunks into separate
    document and metadata lists.
    """

    ordered_documents = [
        item["document"]
        for item in chunks
    ]

    ordered_metadatas = [
        item["metadata"]
        for item in chunks
    ]

    return ordered_documents, ordered_metadatas



def group_chunk_ranges(metadatas):
    """
    Group consecutive chunk numbers into ranges.

    Example:

    [50, 51, 52, 60, 61]

    becomes

    [(50, 52), (60, 61)]
    """

    if not metadatas:
        return []

    chunk_numbers = sorted(
        metadata["chunk_number"]
        for metadata in metadatas
    )

    ranges = []

    start = chunk_numbers[0]
    end = chunk_numbers[0]

    for number in chunk_numbers[1:]:

        if number == end + 1:
            end = number
        else:
            ranges.append((start, end))
            start = number
            end = number

    ranges.append((start, end))

    return ranges




def expand_chunks(documents, metadatas):
    """
    Expand retrieved chunk ranges instead of expanding
    every chunk individually.
    """
    
    if not metadatas:
        return []

    combined = []

    ranges = group_chunk_ranges(metadatas)

    # We need the PDF name to retrieve neighbouring chunks.
    pdf_name = metadatas[0]["pdf_name"]

    for start, end in ranges:

        # expanded_start = max(1, start - 1)
        # expanded_end = end + 1
        expanded_start = max(1, start - CONTEXT_WINDOW)
        expanded_end = end + CONTEXT_WINDOW

        for chunk_number in range(expanded_start, expanded_end + 1):

            chunk = get_chunk_by_number(
                pdf_name,
                chunk_number
            )

            if chunk:
                combined.append(chunk)

    return combined




def prepare_context(documents, metadatas):
    """
    Prepare retrieved chunks for the language model.

    Args:
        documents (list): Retrieved text chunks.
        metadatas (list): Metadata corresponding to each chunk.

    Returns:
        tuple:
            - ordered_documents (list)
            - ordered_metadatas (list)
    """
    expanded_chunks = expand_chunks(
        documents,
        metadatas
    )

    expanded_chunks.sort(
        key=lambda item: (
            item["metadata"]["pdf_name"],
            item["metadata"]["chunk_number"]
        )
    )

    expanded_chunks = remove_duplicates(
        expanded_chunks
    )

    return extract_results(
        expanded_chunks
    )