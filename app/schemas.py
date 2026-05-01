from datetime import date , datetime
from sqlmodel import SQLModel, Field 

class NoteCreate(SQLModel):
    id : int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class NoteRead(SQLModel):
    id: int
    title: str
    content: str
    created_at: datetime

class TaskCreate(SQLModel):
    id : int | None = Field(default=None, primary_key=True)
    text : str
    done : bool = Field(default=False)
    due_date: date | None = None

class TaskRead(SQLModel):
    id: int
    text: str
    done: bool
    due_date: date | None

class NoteUpdate(SQLModel):
    title: str
    content: str 

class TaskUpdate(SQLModel):
    done : bool 

