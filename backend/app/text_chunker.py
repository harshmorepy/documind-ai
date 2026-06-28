from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text, chunk_size=1000, chunk_overlap=200):
    """
    Split text into overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    chunks = splitter.split_text(text)

    return chunks