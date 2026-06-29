# 📄 DocuMind AI

> **An AI-Powered Intelligent Document Assistant built with Python, Google Gemini, and ChromaDB.**

Upload PDF documents, ask questions in natural language, and receive accurate, context-aware answers powered by **Retrieval-Augmented Generation (RAG)** with transparent source citations.

---

# 🌟 Overview

DocuMind AI is an AI application that enables users to interact with PDF documents conversationally.

Instead of manually searching through hundreds of pages, users can simply ask questions in natural language and receive accurate answers generated from the uploaded document.

Unlike traditional chatbots, DocuMind AI grounds every answer using the document itself, making responses more reliable and explainable.

---

# ✨ Features

## Current Features

- 📄 Upload PDF Documents
- 📖 Extract Text from PDFs
- ✂️ Intelligent Text Chunking
- 🧠 Google Gemini Integration
- 🔍 Semantic Search
- 🗂 ChromaDB Vector Database
- 🤖 Retrieval-Augmented Generation (RAG)
- 📚 Source Attribution
- 💬 Interactive Command Line Chat
- ⚡ Fast Document Retrieval

---

# 🚀 Upcoming Features

- 🌐 FastAPI Backend
- 🎨 Modern React Frontend
- 📤 Drag & Drop PDF Upload
- 📑 Multiple PDF Support
- 🖼 Image Extraction
- 📊 Table Understanding
- 🔍 OCR Support
- 🧠 Hybrid Search
- 📈 Context Expansion
- 💾 Chat History
- 🔐 User Authentication
- ☁️ Cloud Deployment
- 🐳 Docker Support

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3 |
| LLM | Google Gemini 2.5 Flash |
| Embeddings | Gemini Embedding Model |
| Vector Database | ChromaDB |
| PDF Processing | PyMuPDF |
| Text Chunking | LangChain Recursive Character Text Splitter |
| Environment Variables | python-dotenv |

---

# 📂 Project Structure

```
documind-ai/
│
├── backend/
│   │
│   ├── app/
│   │   ├── embeddings.py
│   │   ├── pdf_reader.py
│   │   ├── rag.py
│   │   ├── retriever.py
│   │   ├── vector_store.py
│   │   └── text_chunker.py
│   │
│   ├── experiments/
│   │   ├── test_pdf_reader.py
│   │   ├── test_chunking.py
│   │   ├── test_embedding.py
│   │   ├── test_vector_store.py
│   │   ├── test_retriever.py
│   │   └── test_rag.py
│   │
│   └── uploads/
│
├── design/
│   └── screenshots/
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/documind-ai.git

cd documind-ai
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create Environment File

Create a `.env` file in the root directory.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## 5️⃣ Run DocuMind AI

```bash
python -m backend.experiments.test_rag
```

---

# 🧠 How It Works

```
                 User Question
                        │
                        ▼
             Generate Query Embedding
                        │
                        ▼
            Search ChromaDB Vector Store
                        │
                        ▼
             Retrieve Relevant Chunks
                        │
                        ▼
             Build Prompt with Context
                        │
                        ▼
             Google Gemini 2.5 Flash
                        │
                        ▼
               Generate Final Answer
                        │
                        ▼
             Display Source Citations
```

---

# 💬 Example

```
👤 You:

What is Python?

------------------------------------------------------------

🤖 DocuMind AI

Python is a high-level, general-purpose programming language
developed by Guido van Rossum in 1991.

Key Features

• Object-Oriented
• Interpreted
• Easy to Learn
• Portable
• Powerful
• Open Source

------------------------------------------------------------

📚 Sources

• python_notes.pdf (Chunk 10)

• python_notes.pdf (Chunk 11)

• python_notes.pdf (Chunk 12)
```

---

# 📈 Development Progress

## ✅ Version v0.4.0

### Completed

- ✅ Project Initialization
- ✅ Google Gemini Integration
- ✅ PDF Text Extraction
- ✅ Intelligent Chunking
- ✅ Embedding Generation
- ✅ ChromaDB Integration
- ✅ Semantic Search
- ✅ Retriever
- ✅ Prompt Engineering
- ✅ Complete RAG Pipeline
- ✅ Source Attribution
- ✅ Interactive Chat Interface

---

# 🗺 Roadmap

| Version | Milestone | Status |
|----------|-----------|--------|
| v0.1.0 | Project Setup | ✅ |
| v0.2.0 | Gemini Integration | ✅ |
| v0.3.0 | Embeddings & ChromaDB | ✅ |
| v0.4.0 | Complete RAG Pipeline | ✅ |
| v0.5.0 | Advanced Retrieval | 🔄 |
| v0.6.0 | FastAPI Backend | ⏳ |
| v0.7.0 | React Frontend | ⏳ |
| v0.8.0 | Multi-PDF Chat | ⏳ |
| v0.9.0 | Image & Table Understanding | ⏳ |
| v1.0.0 | Production Release | 🚀 |

---

# 🎯 Vision

DocuMind AI is more than just a PDF chatbot.

Our goal is to build an intelligent AI assistant capable of understanding:

- 📄 Documents
- 📊 Tables
- 🖼 Images
- 📈 Charts
- 📐 Diagrams

while providing trustworthy answers with complete source attribution.

The long-term vision is to create an AI assistant that professionals, students, researchers, and businesses can rely on every day.

---

# 🤝 Contributing

Contributions, ideas, feature requests, and feedback are always welcome.

If you'd like to improve DocuMind AI:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.

Every star motivates further development and helps more people discover the project.

---

# 👨‍💻 Author

**Harsh More**

B.Tech Computer Science & Engineering

Building modern AI applications using Python, Cloud, and Generative AI.

---

# 🚀 Thank You

Thank you for visiting **DocuMind AI**.

This project is being built in public, one milestone at a time.

Every commit represents a step toward creating a production-ready AI document assistant.

If you're following this journey, don't forget to ⭐ the repository and check back for future updates.

## ⭐ Happy Coding!