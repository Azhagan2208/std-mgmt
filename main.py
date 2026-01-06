from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management")


# DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create student
@app.post("/students/")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)


# Read all
@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)


# Read one
@app.get("/students/{id}")
def get_student(id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, id)
    if not student:
        raise HTTPException(404, "Student not found")
    return student


# update
@app.put("/students/{student_id}")
def update_student(
    student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)
):
    updated_student = crud.update_student(db, student_id, student)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student


# Delete
@app.delete("/students/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):
    student = crud.delete_student(db, id)
    if not student:
        raise HTTPException(404, "Student not found")
    return {"message": "Deleted"}
