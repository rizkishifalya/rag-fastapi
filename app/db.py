import os
import asyncpg

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:example@localhost:5432/ragdb")

_pool = None

async def init_db_pool():
    global _pool
    if _pool is None:
        _pool = await asyncpg.create_pool(DATABASE_URL)
    return _pool

async def close_db_pool():
    global _pool
    if _pool:
        await _pool.close()
        _pool = None

def get_db():
    return _pool
