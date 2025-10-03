from sqlmodel import SQLModel, create_engine, Session

# Sesuaikan user/password/database dengan punya kamu
DATABASE_URL = "postgresql+psycopg2://postgres:example@localhost:5432/ragdb"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    # Membuat semua tabel (hanya dipakai kalau tanpa alembic)
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
