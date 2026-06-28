from backend.app.pdf_reader import extract_text
from backend.app.text_chunker import chunk_text


text = extract_text("data/pdfs/python_notes.pdf")

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")
print(f"Length of First Chunk: {len(chunks[0])}")

# print("\nFirst 300 characters of Chunk 1:\n")
# print(chunks[0][:300])

# print("\nLast 300 characters of Chunk 1:\n")
# print(chunks[0][:-300])

# print("\nFirst 300 characters of Chunk 2:\n")
# print(chunks[1][:300])

# chunk_number = 20

# print(f"\nLast 300 characters of Chunk {chunk_number + 1}:\n")
# print(chunks[chunk_number][-300:])

# print(f"\nFirst 300 characters of Chunk {chunk_number + 2}:\n")
# print(chunks[chunk_number + 1][:300])

# print(f"\nTotal Chunks: {len(chunks)}\n")

for index, chunk in enumerate(chunks, start=1):
    print("=" * 60)
    print(f"Chunk {index}")
    print("=" * 60)
    print(chunk)
    print()