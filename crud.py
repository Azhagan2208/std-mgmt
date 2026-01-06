from sqlalchemy.orm import Session
from models import Student
import schemas

def create_student(db: Session, data: schemas.StudentCreate):
    student = Student(name=data.name, age=data.age, course=data.course)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_students(db: Session):
    return db.query(Student).all()


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)
    if student:
        db.delete(student)
        db.commit()
    return student

def update_student(db: Session, student_id: int, new_data):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student:
        student.name = new_data.name
        student.age = new_data.age
        student.course = new_data.course

        db.commit()
        db.refresh(student)
        return student
    return None

