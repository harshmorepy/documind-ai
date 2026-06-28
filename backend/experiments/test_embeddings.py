from backend.app.embeddings import get_embedding

text = "Python is one of the easiest programming languages."

embedding = get_embedding(text)

print(f"Embedding Length: {len(embedding)}")

print("\nFirst 10 Values:\n")

print(embedding[:10])