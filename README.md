# RAG-FastAPI - skeleton

Repo skeleton untuk prototipe RAG (Retrieval-Augmented Generation) menggunakan FastAPI + Postgres.

## Run

1. docker compose up -d
2. python -m venv .venv
3. source .venv/bin/activate # (Windows: .venv\Scripts\activate)
4. pip install -r requirements.txt
5. uvicorn app.main:app --reload --port 8000

## Endpoints

- POST /ingest/ -> { "content": "...", "title": "...", "metadata": {...} }
- POST /query/ -> { "query": "...", "top_k": 5 }

Apa itu RAG (Retrieval Augmented Generation)
→ konsep: LLM ditambah database/vector store untuk recall pengetahuan eksternal.

Postgres + pgvector
→ extension untuk simpan & cari embedding vector (mirip FAISS/Weaviate tapi langsung di Postgres).

Postgres + pg_bigm
→ extension untuk full-text search dengan trigram/bigram matching (berguna untuk keyword search cepat).

Hybrid approach
→ bisa gabungkan semantic search (pgvector) + keyword search (pg_bigm) untuk hasil lebih bagus.
