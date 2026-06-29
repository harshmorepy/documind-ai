from backend.app.retriever import retrieve

query = "What is Python?"

results = retrieve(query)

print(results)

print("=" * 80)
print(f"Query: {query}")
print("=" * 80)

documents = results["documents"][0]

for i, doc in enumerate(documents, start=1):
    print(f"\nResult {i}")
    print("-" * 80)
    print(doc[:500])      # Print first 500 characters