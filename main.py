from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    name: str
    email: str
    age: int
    roll_no: str
    department: str
    
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
    rollno: str
    department: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

def create_student(student: Student):
    return Student

def read_student(id: int):
    return StudentResponse(id=id, **student.dict())

def update_student(id: int, student: Student):
    return StudentResponse(id=id, **student.dict())

def delete_student(id: int):
    return StudentResponse(id=id, **student.dict())

@app.post("/students")
def create_student(student: Student):
    return create_student(student)

@app.get("/students/{id}")
def read_student(id: int):
    return read_student(id)

@app.put("/students/{id}")
def update_student(id: int, student: Student):
    return update_student(id, student)

@app.delete("/students/{id}")
def delete_student(id: int):
    return delete_student(id)