from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Task(BaseModel):
    name: str
    description: Optional [str] = None

@app.get("/tasks")
def get_my_tasks():
    task = Task(name = "давай создадим проект")
    return {"data": task}
