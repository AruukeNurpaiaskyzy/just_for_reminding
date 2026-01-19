from fastapi import FastAPI, HTTPException
from project.models import Movie
from typing import List
from pydantic import BaseModel
# from pydantic import BaseModel
# from typing import Optional, Annotated
# from fastapi import Depends, HTTPException

app = FastAPI()

class Movie(BaseModel):
    id: int
    title: str
    description: str

# Пример базы данных
movies_db = [
    Movie(id=1, title="Фильм 1", description="Описание 1"),
    Movie(id=2, title="Фильм 2", description="Описание 2"),
    Movie(id=3, title="Фильм 3", description="Описание 3"),
]

# @app.get('/')
# def read_root():
#     return{'Hello': 'Aruuke'}
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

# @app.get('/movies/', response_model=list[Movie])
# def get_movie():
#     return movies_db
# # class Task(BaseModel):

# @app.get('/movies{movie_id}/', response_model=list[Movie])
# def get_movie_by_id(movie_id:int):
#     if movie_id < 0 or movie_id > len(movies_db):
#         raise HTTPException(status_code=404, detail='Movie not found')
#     return movies_db[movie_id - 1]
# # class Task(BaseModel):


@app.get('/movies/', response_model=List[Movie])
def get_movies():
    return movies_db

@app.get('/movies/{movie_id}', response_model=Movie)
def get_movie_by_id(movie_id: int):
    # Ищем фильм по ID (а не по индексу массива)
    for movie in movies_db:
        if movie.id == movie_id:
            return movie
    
    # Если не нашли, выбрасываем исключение
    raise HTTPException(status_code=404, detail='Movie not found')

