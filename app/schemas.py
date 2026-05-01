from datetime import date , datetime
from sqlmodel import SQLModel, Field 

class NoteCreate(SQLModel):
    title: str
    content: str

class NoteRead(SQLModel):
    id: int
    title: str
    content: str
    created_at: datetime

