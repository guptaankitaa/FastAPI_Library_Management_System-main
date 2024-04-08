
from fastapi import FastAPI
from api.endpoints import students

app = FastAPI()

app.include_router(students.router, prefix="/students", tags=["students"])
