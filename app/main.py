from fastapi import FastAPI
from app.api import ingest, query
from app.db import init_db_pool, close_db_pool

app = FastAPI(title="RAG FastAPI Prototype")

app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
app.include_router(query.router, prefix="/query", tags=["query"])

@app.on_event("startup")
async def on_startup():
    await init_db_pool()

@app.on_event("shutdown")
async def on_shutdown():
    await close_db_pool()
