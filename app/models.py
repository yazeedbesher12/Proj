from sqlmodel import SQLModel, Field
from datetime import date, datetime

class Note(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    text : str
    done : bool = Field(default=False)
    due_date: date | None = None
   