from fastapi import APIRouter
from pydantic import BaseModel
from app.embeddings import create_embedding
from app.db import get_db
import math

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5

def cosine_sim(a, b):
    # safety if lengths differ -> zip shortest
    dot = sum(x*y for x,y in zip(a,b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(y*y for y in b))
    return dot / (na*nb) if na and nb else 0.0

@router.post("/")
async def query(req: QueryRequest):
    pool = get_db()
    if pool is None:
        return {"error": "db not initialized"}
    qemb = create_embedding(req.query)
    rows = await pool.fetch("SELECT id, title, content, metadata, embedding FROM documents")
    results = []
    for r in rows:
        doc_emb = r["embedding"] or []
        score = cosine_sim(qemb, doc_emb)
        results.append({
            "id": r["id"],
            "title": r["title"],
            "score": score,
            "content": r["content"]
        })
    results.sort(key=lambda x: x["score"], reverse=True)
    return {"results": results[: req.top_k]}
