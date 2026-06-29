from backend.app.vector_store import collection
from backend.app.embeddings import get_embedding


def retrieve(query, n_results=10):
    """
    Retrieve the most relevant chunks for a user query.
    """

    # Convert question into embedding
    query_embedding = get_embedding(query)

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    return {
       "documents": documents,
       "metadatas": metadatas
    }