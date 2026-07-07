from backend.app.vector_store import collection
from backend.app.embeddings import get_embedding
from backend.app.core.constants import TOP_K_RESULTS


def retrieve(
    query,
    document: str | None = None,
    n_results=TOP_K_RESULTS,
):
    """
    Retrieve the most relevant chunks for a user query.
    """

    # Convert question into embedding
    query_embedding = get_embedding(query)
    
    
    
    query_params = {
        "query_embeddings": [query_embedding],
        "n_results": n_results,
        "include": [
            "documents",
            "metadatas",
            "distances",
        ],
    }
    
    if document:
        query_params["where"] = {
            "pdf_name": document
        }

    # Search ChromaDB
    results = collection.query(**query_params)
    # print("Metadatas:")
    # print(results["metadatas"])

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    return {
       "documents": documents,
       "metadatas": metadatas,
       "distances": distances
    }