import chromadb
from pathlib import Path
from backend.app.core.constants import COLLECTION_NAME


# Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="data/chroma_db")

# Create (or get) a collection
collection_name = COLLECTION_NAME



collection = client.get_or_create_collection(
    name=collection_name
)


def add_chunks(chunks, embeddings, pdf_name):
    """
    Store chunks and their embeddings in ChromaDB.
    """
    document_name = Path(pdf_name).stem
    document_name = document_name.replace(" ", "_").lower()

    ids = [f"{document_name}_chunk_{i}" for i in range(len(chunks))]
    metadatas = []

    for i in range(len(chunks)):
        metadatas.append(
            {
                "pdf_name": document_name,
                "chunk_index": i,
                "chunk_number": i + 1,
                "total_chunks": len(chunks)
            }
        )

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )


def get_collection_count():
    """
    Return the number of stored chunks.
    """
    return collection.count()

def get_chunk_by_number(pdf_name, chunk_number):
    """
    Retrieve a specific chunk from a document using its chunk number.

    Args:
        pdf_name (str): Name of the indexed PDF.
        chunk_number (int): Chunk number to retrieve.

    Returns:
        dict | None:
            {
                "document": ...,
                "metadata": ...
            }

            Returns None if the chunk is not found.
    """

    results = collection.get(
        where={
            "$and": [
                {"pdf_name": pdf_name},
                {"chunk_number": chunk_number}
            ]
        },
        limit=1
    )

    if len(results["documents"]) == 0:
        return None

    return {
        "document": results["documents"][0],
        "metadata": results["metadatas"][0]
    }