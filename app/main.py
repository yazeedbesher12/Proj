from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from fastapi import Depends

from db import create_db_and_tables, get_session
from models import Task, Note

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/Notes/", status_code=201)
def create_note(note: Note, session: Session = Depends(get_session)):
    session.add(note)
    session.commit()
    session.refresh(note)
    return note

@app.post("/Tasks/",status_code=201)
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

@app.get("/Notes/{note_id}")
def read_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if note :
      return note
    raise HTTPException(status_code=404, detail="Note not found")

@app.put("/Notes/{note_id}")
def update_note(note_id: int, note: Note, session: Session = Depends(get_session)):
    existing_note = session.get(Note, note_id)
    if existing_note:
        existing_note.title = note.title
        existing_note.content = note.content
        session.add(existing_note)
        session.commit()
        session.refresh(existing_note)
        return existing_note
    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/Notes/{note_id}")
def delete_note(note_id : int , session : Session = Depends(get_session)):
    note = session.get(Note,note_id)
    if note:
        session.delete(note)
        session.commit()
        return {"message": "Note deleted successfully"}
    raise HTTPException(status_code=404, detail="Note not found")


@app.delete("/Tasks/{task_id}")
def delete_task(task_id : int , session : Session = Depends(get_session)):
    task = session.get(Task,task_id)
    if task : 
        session.delete(task)
        session.commit()
        return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

@app.patch("/Tasks/{task_id}")
def update_task(task_id : int , task : Task , session : Session = Depends(get_session)):
    existing_task = session.get(Task,task_id)
    if existing_task:
        existing_task.done = task.done
        session.add(existing_task)
        session.commit()
        session.refresh(existing_task)
        return existing_task
    raise HTTPException(status_code=404, detail="Task not found")


