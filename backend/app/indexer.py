import os
from backend.app.pdf_reader import extract_text
from backend.app.text_chunker import chunk_text
from backend.app.embeddings import get_embedding
from backend.app.vector_store import add_chunks


def index_pdf(pdf_path):
    """
    Complete indexing pipeline for a PDF.
    """

    print("📄 Reading PDF...")
    text = extract_text(pdf_path)

    print("✂️ Splitting into chunks...")
    chunks = chunk_text(text)

    print(f"📚 Total chunks: {len(chunks)}")

    embeddings = []

    for index, chunk in enumerate(chunks, start=1):
        print(f"Generating embedding {index}/{len(chunks)}")
        embeddings.append(get_embedding(chunk))

    print("💾 Storing in ChromaDB...")
    add_chunks(
    chunks,
    embeddings,
    os.path.basename(pdf_path)
)
    print("✅ PDF indexed successfully!")