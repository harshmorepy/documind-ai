from backend.app.pdf_reader import extract_text
from backend.app.text_chunker import chunk_text
from backend.app.embeddings import get_embedding
from backend.app.vector_store import add_chunks, get_collection_count

# Step 1: Read the PDF
text = extract_text("data/pdfs/python_notes.pdf")

# Step 2: Split into chunks
chunks = chunk_text(text)

# Step 3: Generate embeddings for every chunk
embeddings = []

for i, chunk in enumerate(chunks, start=1):
    print(f"Generating embedding {i}/{len(chunks)}...")
    embeddings.append(get_embedding(chunk))

# Step 4: Store in ChromaDB
add_chunks(chunks, embeddings)

# Step 5: Verify
print(f"\nTotal Stored Chunks: {get_collection_count()}")