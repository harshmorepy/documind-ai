from backend.app.retriever import retrieve
from backend.app.context_expander import prepare_context
from backend.app.prompts.qa_prompt import build_qa_prompt

from google import genai
import os
from dotenv import load_dotenv

from backend.app.schemas import document
from pathlib import Path


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def answer_question(
    question: str,
    document: str | None = None,
):
    
    if document:
        document = Path(document).stem
        document = document.replace(" ", "_").lower()
    
    results = retrieve(
        query=question,
        document=document,
    )
    
    

    chunks = results["documents"]
    metadata = results["metadatas"]

    chunks, metadata = prepare_context(
        chunks,
        metadata
    )

    context = "\n\n".join(chunks)
    
    sources = []

    for item in metadata:
        sources.append(
            f"{item['pdf_name']} (Chunk {item['chunk_number']})"
        )

    sources = "\n".join(sources)

    prompt = build_qa_prompt(
        context=context,
        question=question
    )
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

    except Exception as error:
        print(f"❌ Gemini API Error: {error}")

        return {
            "success": False,
            "answer": (
                "The AI service is temporarily unavailable. "
                "Please try again in a few moments."
            ),
            "sources": []
        }

    return {
        "success": True,
        "answer": response.text,
        "sources": sources
    }