from fastapi import APIRouter
from pydantic import BaseModel
from app.embeddings import create_embedding
from app.db import get_db
import json

router = APIRouter()

class IngestRequest(BaseModel):
    content: str
    title: str = None
    metadata: dict = None

@router.post("/")
async def ingest(req: IngestRequest):
    pool = get_db()
    if pool is None:
        return {"error": "db not initialized"}
    emb = create_embedding(req.content)
    # store embedding as jsonb
    await pool.execute(
        "INSERT INTO documents (title, content, metadata, embedding) VALUES ($1,$2,$3::jsonb,$4::jsonb)",
        req.title,
        req.content,
        json.dumps(req.metadata or {}),
        json.dumps(emb)
    )
    return {"status": "ok"}
