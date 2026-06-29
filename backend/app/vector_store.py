import chromadb

# Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="data/chroma_db")

# Create (or get) a collection
collection_name = "documind_documents"

# try:
#     client.delete_collection(collection_name)
# except Exception:
#     pass

collection = client.get_or_create_collection(
    name=collection_name
)


def add_chunks(chunks, embeddings, pdf_name):
    """
    Store chunks and their embeddings in ChromaDB.
    """

    ids = [f"chunk_{i}" for i in range(len(chunks))]
    metadatas = []

    for i in range(len(chunks)):
        metadatas.append(
            {
                "pdf_name": pdf_name,
                "chunk_number": i + 1
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