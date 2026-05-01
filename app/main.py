from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from fastapi import Depends

from app.db import create_db_and_tables, get_session
from app.models import Task, Note
from app.schemas import NoteCreate, NoteRead, TaskCreate, TaskRead, NoteUpdate, TaskUpdate

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/Notes/", status_code=201,response_model=NoteRead)
def create_note(note: NoteCreate, session: Session = Depends(get_session)):
    db_note = Note(title=note.title, content=note.content)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note

@app.post("/Tasks/",status_code=201,response_model=TaskRead)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    db_task = Task(text=task.text, done=task.done, due_date=task.due_date)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@app.get("/Notes/",response_model=list[NoteRead])
def read_notes(session: Session = Depends(get_session)):
    notes = session.exec(select(Note)).all()
    return notes

@app.get("/Tasks/",response_model=list[TaskRead])
def read_tasks(session: Session = Depends(get_session)):    
    tasks = session.exec(select(Task)).all()
    return tasks

@app.get("/Notes/{note_id}", response_model=NoteRead)
def read_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if note :
      return note
    raise HTTPException(status_code=404, detail="Note not found")

@app.put("/Notes/{note_id}",response_model=NoteRead)
def update_note(note_id: int, note: NoteUpdate, session: Session = Depends(get_session)):
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

@app.patch("/Tasks/{task_id}",response_model=TaskRead)
def update_task(task_id : int , task : TaskUpdate , session : Session = Depends(get_session)):
    existing_task = session.get(Task,task_id)
    if existing_task:
        existing_task.done = task.done
        session.add(existing_task)
        session.commit()
        session.refresh(existing_task)
        return existing_task
    raise HTTPException(status_code=404, detail="Task not found")


