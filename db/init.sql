-- Minimal DB init (works without pgvector)
CREATE TABLE IF NOT EXISTS documents (
  id serial PRIMARY KEY,
  title text,
  content text,
  metadata jsonb,
  embedding jsonb
);
