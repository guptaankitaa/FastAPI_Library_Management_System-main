from fastapi import APIRouter, HTTPException
from ..db.connections import students_collection
from ..models.student import Student
from bson.objectid import ObjectId

router = APIRouter()

@router.post("/", status_code=201)
async def create_student(student: Student):
    inserted_student = students_collection.insert_one(student.dict())
    return {"id": str(inserted_student.inserted_id)}

@router.get("/", status_code=200)
async def list_students(country: str = None, age: int = None):
    filters = {}
    if country:
        filters["address.country"] = country
    if age:
        filters["age"] = {"$gte": age}
    result = list(students_collection.find(filters, {"_id": 0}))
    return {"data": result}

@router.get("/{id}", status_code=200)
async def get_student(id: str):
    student = students_collection.find_one({"_id": ObjectId(id)}, {"_id": 0})
    if student:
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@router.patch("/{id}", status_code=204)
async def update_student(id: str, student: Student):
    result = students_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": student.dict(exclude_unset=True)}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return

@router.delete("/{id}", status_code=200)
async def delete_student(id: str):
    result = students_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return