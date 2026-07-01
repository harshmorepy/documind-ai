from backend.app.retriever import retrieve

query = input("Enter your question: ")

results = retrieve(query)

documents = results["documents"]
metadatas = results["metadatas"]
distances = results["distances"]

print("\n" + "=" * 80)
print("Retrieval Results")
print("=" * 80)

for i, (metadata, distance) in enumerate(
    zip(metadatas, distances),
    start=1
):
    print(f"\nResult #{i}")
    print(f"PDF      : {metadata['pdf_name']}")
    print(f"Chunk    : {metadata['chunk_number']}")
    print(f"Distance : {distance:.6f}")

print("\n" + "=" * 80)