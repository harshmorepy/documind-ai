from backend.app.retriever import retrieve
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def answer_question(question):

    results = retrieve(question)
    
    # print("=" * 50)
    # print("DEBUG")
    # print("=" * 50)
    
    # print(results)

    # print(type(results["documents"]))
    # print(results["documents"])

    # print(type(results["documents"][0]))

    # if isinstance(results["documents"][0], list):
    #     print("The first item is a LIST")
    # else:
    #     print("The first item is a STRING")

    chunks = results["documents"]
    metadata = results["metadatas"]

    context = "\n\n".join(chunks)
    
    sources = []

    for item in metadata:
        sources.append(
            f"{item['pdf_name']} (Chunk {item['chunk_number']})"
        )

    sources = "\n".join(sources)

    prompt = f"""
You are a helpful AI assistant.

You are DocuMind AI, an intelligent document assistant.

Your task is to answer ONLY using the provided document context.

Instructions:

- Read ALL retrieved chunks carefully.
- Combine information from multiple chunks into one complete answer.
- Do not omit important details.
- If examples exist in the document, include them.
- If the document provides advantages, disadvantages, notes, or warnings, include them.
- Format your response with headings and bullet points where appropriate.
- If the answer is not present in the document, respond:
  "I couldn't find that information in the uploaded document."

If the answer is not found in the context,
say:

"I couldn't find that information in the document."

Context:

{context}

Question:

{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "answer": response.text,
        "sources": sources
    }