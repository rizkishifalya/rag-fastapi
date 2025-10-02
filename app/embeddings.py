import os
import hashlib
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def create_embedding(text: str):
    """
    Jika OPENAI_API_KEY tersedia, akan panggil OpenAI Embeddings.
    Kalau tidak, fallback: buat vector sederhana (hash -> numbers) supaya pipeline bisa dites offline.
    """
    if OPENAI_API_KEY:
        resp = requests.post(
            "https://api.openai.com/v1/embeddings",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
            json={"model": "text-embedding-3-small", "input": text}
        )
        resp.raise_for_status()
        return resp.json()["data"][0]["embedding"]
    else:
        # fallback deterministic short vector (32 dims) - untuk testing
        h = hashlib.sha256(text.encode()).digest()
        return [b / 255.0 for b in h]  # list of floats
