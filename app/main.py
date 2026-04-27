from fastapi import fastapi
from sqlmodel import Session, select
from fastapi import Depends

from db import create_db_and_tables, get_session
from models import User

app = fastapi()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/Notes/")
def create_note(note: Note, session: Session = Depends(get_session)):
    session.add(note)
    session.commit()
    session.refresh(note)
    return note

@app.post("/Tasks/")
def create_task(task: Task, session: Session = Depends(get_session)):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@app.get("/Notes/")
def read_notes(session: Session = Depends(get_session)):
    notes = session.exec(select(Note)).all()
    return notes

@app.get("/Tasks/")
def read_tasks(session: Session = Depends(get_session)):    
    tasks = session.exec(select(Task)).all()
    return tasks

