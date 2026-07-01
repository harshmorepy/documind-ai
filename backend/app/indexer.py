from pathlib import Path
from backend.app.pdf_reader import extract_text
from backend.app.text_chunker import chunk_text
from backend.app.embeddings import get_embedding
from backend.app.vector_store import add_chunks
from backend.app.core.logging import logger


def index_pdf(pdf_path):
    """
    Complete indexing pipeline for a PDF.

    Returns:
        dict: Information about the indexing result.
    """

    try:
        logger.info("📄 Reading PDF...")
        text = extract_text(pdf_path)

        logger.info("✂️ Splitting into chunks...")
        chunks = chunk_text(text)

        logger.info(f"📚 Total chunks: {len(chunks)}")

        embeddings = []

        for index, chunk in enumerate(chunks, start=1):
            logger.info(f"Generating embedding {index}/{len(chunks)}...")
            embeddings.append(get_embedding(chunk))

        document_name = Path(pdf_path).name

        logger.info("💾 Storing in ChromaDB...")
        add_chunks(
            chunks,
            embeddings,
            document_name
        )

        logger.info("✅ PDF indexed successfully!")

        return {
            "status": "success",
            "pdf_name": document_name,
            "total_chunks": len(chunks),
        }

    except Exception as error:
        logger.error(f"❌ Indexing failed: {error}")

        return {
            "status": "failed",
            "error": str(error),
        }