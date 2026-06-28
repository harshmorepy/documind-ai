import chromadb

# Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="data/chroma_db")

# Create (or get) a collection
collection = client.get_or_create_collection(
    name="documind_documents"
)


def add_chunks(chunks, embeddings):
    """
    Store chunks and their embeddings in ChromaDB.
    """

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
    )


def get_collection_count():
    """
    Return the number of stored chunks.
    """
    return collection.count()