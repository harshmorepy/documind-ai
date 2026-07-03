![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-009688?logo=fastapi)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-orange)
![Gemini](https://img.shields.io/badge/LLM-Gemini%202.5%20Flash-blueviolet)
![License](https://img.shields.io/badge/License-MIT-success)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)
![Version](https://img.shields.io/badge/Version-v0.6.0-blue)


## 📊 Project Snapshot

| Metric | Value |
|---------|-------|
| Version | v0.6.0 |
| Development Status | Active |
| Language | Python 3.13 |
| Backend | FastAPI |
| LLM | Gemini 2.5 Flash |
| Vector Database | ChromaDB |
| Architecture | Modular RAG |
| License | MIT |


## 🎯 Why DocuMind AI?

Traditional chatbots cannot reliably answer questions about private documents because they lack access to the document's content.

DocuMind AI solves this by combining Retrieval-Augmented Generation (RAG), vector embeddings, and Large Language Models to produce grounded, document-aware answers while citing the relevant source chunks.


## ⭐ Highlights

- Production-oriented architecture
- FastAPI REST backend
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Context Expansion
- Source Citations
- Modular Services
- Clean Architecture
- Ready for Cloud Deployment


## 🧩 Core Components


| Module              | Responsibility             |
| ------------------- | -------------------------- |
| pdf_reader.py       | Extract PDF text           |
| text_chunker.py     | Split documents            |
| embeddings.py       | Generate vector embeddings |
| vector_store.py     | ChromaDB integration       |
| retriever.py        | Semantic search            |
| context_expander.py | Improve retrieval context  |
| rag.py              | RAG orchestration          |
| rag_service.py      | Business logic             |
| chat.py             | REST API endpoint          |


## 🏗️ System Architecture Diagram 

               User
                  │
                  ▼
         FastAPI REST API
                  │
         ┌────────┴────────┐
         ▼                 ▼
     Chat API         Upload API
         │                 │
         └────────┬────────┘
                  ▼
            Service Layer
                  │
                  ▼
            RAG Engine
                  │
         ┌────────┴─────────┐
         ▼                  ▼
    Retriever         PDF Indexer
         │                  │
         ▼                  ▼
 Context Expansion     Chunking
         │                  │
         └────────┬─────────┘
                  ▼
             ChromaDB
                  │
                  ▼
               Gemini
                  │
                  ▼
          Final AI Response
                

## 📜 Version History

### v0.6.0

- FastAPI Backend
- Swagger UI
- REST API
- Service Layer
- Clean Architecture

### v0.5.0

- Context Expansion
- Improved Retrieval
- Prompt Refactoring

### v0.4.0

- ChromaDB
- Semantic Search

### v0.3.0

- Embedding Generation

### v0.2.0

- Text Chunking

### v0.1.0

- PDF Reader



## 🎯 Next Milestone (v0.7.0)

- Upload API
- Automatic Indexing
- File Validation
- Multi-document Support

## 🎯 Future Milestones

- Authentication
- Chat History
- Streamlit Frontend
- Docker
- AWS Deployment
- CI/CD
- Monitoring


## 💼 What This Project Demonstrates

- AI Engineering
- Backend Development
- FastAPI
- REST APIs
- Vector Databases
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Software Architecture
- Git Workflow
- Production-Oriented Development


## 📚 Development Philosophy

DocuMind AI is intentionally built in incremental milestones.

Every feature is designed, implemented, tested, refactored, documented, and committed before moving to the next stage.

This mirrors how production software is developed in professional engineering teams.


---

## 🌟 Thank You

Thank you for taking the time to explore DocuMind AI.

This project represents an ongoing journey toward building production-ready AI systems with clean architecture, scalable backend engineering, and modern Large Language Models.

Whether you're a recruiter, developer, or AI enthusiast, I hope this repository provides insight into both the engineering process and the evolution of an AI application from prototype to production.

If you find the project interesting:

⭐ Star the repository

🍴 Fork it

💬 Share feedback

🚀 Follow the journey

Happy Coding!

— Harsh More