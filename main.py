from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Annotated
from fastapi import Depends, HTTPException

app = FastAPI()


class Task(BaseModel):
    name: str
    description: Optional [str] = None
class STaskAdd(BaseModel):
    name:str
    description: Optional [str] = None

class STask(STaskAdd):
    id:int

tasks = []


@app.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return{"ok": True}

# @app.get("/tasks")
# def get_tasks():
#     task = Task(name = "давай создадим проект")
#     return {"data": task}
