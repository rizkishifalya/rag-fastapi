from typing import Optional, List
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSON

class Document(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    embedding: Optional[List[float]] = Field(
        sa_column=Column(JSON)  # simpan list float sebagai JSON
    )
