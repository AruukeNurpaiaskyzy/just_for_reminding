from fastapi import FastAPI, HTTPException
from project.models import Movie
# from pydantic import BaseModel
# from typing import Optional, Annotated
# from fastapi import Depends, HTTPException

app = FastAPI(title = 'Movies API')
movies_db = [
    Movie(title='Movie 1', year=2021, description='Movie 1' ),
    Movie(title='Movie 2', year=2022, description='Movie 2' ),
    Movie(title='Movie 3', year=2023, description='Movie 3' ),
    Movie(title='Movie 4', year=2024, description='Movie 4' ),
    Movie(title='Movie 5', year=2025, description='Movie 5' ),
]
@app.get('/')
def read_root():
    return{'Hello': 'Aruuke'}
# class Task(BaseModel):
#     name: str
#     description: Optional [str] = None
# class STaskAdd(BaseModel):
#     name:str
#     description: Optional [str] = None

# class STask(STaskAdd):
#     id:int

# tasks = []


# @app.post("/tasks")
# async def add_task(
#     task: Annotated[STaskAdd, Depends()],
# ):
#     tasks.append(task)
#     return{"ok": True}

# @app.get("/tasks")
# def get_tasks():
#     task = Task(name = "давай создадим проект")
#     return {"data": task}

@app.get('/movies/', response_model=list[Movie])
def get_movie():
    return movies_db
# class Task(BaseModel):

@app.get('/movies{movie_id}/', response_model=list[Movie])
def get_movie_by_id(movie_id:int):
    if movie_id < 0 or movie_id > len(movies_db):
        raise HTTPException(status_code=404, detail='Movie not found')
    return movies_db[movie_id]
# class Task(BaseModel):


