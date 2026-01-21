# from fastapi import FastAPI, HTTPException, Query
# from typing import List, Optional
# from pydantic import BaseModel
# # from pydantic import BaseModel
# # from typing import Optional, Annotated
# # from fastapi import Depends, HTTPException

# app = FastAPI()

# class Movie(BaseModel):
#     id: int
#     title: str
#     description: str
#     year: Optional[int] = None

# # Пример базы данных
# movies_db = [
#     Movie(id=1, title="Фильм1", description="Описание 1", year=2020),
#     Movie(id=2, title="Фильм2", description="Описание 2", year=2022),
#     Movie(id=3, title="Фильм3", description="Описание 3", year=2020),
# ]

# # @app.get('/')
# # def read_root():
# #     return{'Hello': 'Aruuke'}
# # class Task(BaseModel):
# #     name: str
# #     description: Optional [str] = None
# # class STaskAdd(BaseModel):
# #     name:str
# #     description: Optional [str] = None

# # class STask(STaskAdd):
# #     id:int

# # tasks = []


# # @app.post("/tasks")
# # async def add_task(
# #     task: Annotated[STaskAdd, Depends()],
# # ):
# #     tasks.append(task)
# #     return{"ok": True}

# # @app.get("/tasks")
# # def get_tasks():
# #     task = Task(name = "давай создадим проект")
# #     return {"data": task}

# # @app.get('/movies/', response_model=list[Movie])
# # def get_movie():
# #     return movies_db
# # # class Task(BaseModel):

# # @app.get('/movies{movie_id}/', response_model=list[Movie])
# # def get_movie_by_id(movie_id:int):
# #     if movie_id < 0 or movie_id > len(movies_db):
# #         raise HTTPException(status_code=404, detail='Movie not found')
# #     return movies_db[movie_id - 1]
# # # class Task(BaseModel):


# @app.get('/movies/', response_model=List[Movie])
# def get_movies(
#     year:Optional[int] = Query(default=None, description='Год релиза'),
#     title:Optional[str] = Query(default=None, description='название фильма')
# ):                                                                                                      
#     results = movies_db
#     if year is not None:
#         results = [movie for movie in results if movie.year == year]
#     if title is not None:
#         results = [movie for movie in results if movie.title == title]
#     return results

# @app.get('/movies/{movie_id}', response_model=Movie)
# def get_movie_by_id(movie_id: int):
#     # Ищем фильм по ID (а не по индексу массива)
#     for movie in movies_db:
#         if movie.id == movie_id:
#             return movie
    
#     # Если не нашли, выбрасываем исключение
#     raise HTTPException(status_code=404, detail='Movie not found')

# @app.post('/movies/', response_model=Movie, status_code=201)
# def create_movie(movie: Movie):
#     for m in movies_db:
#         if m.id == movie.id:
#             raise HTTPException(status_code=400, detail='уже существует')
#     for m in movies_db:
#         if (m.title.lower() == movie.title.lower() and 
#             m.year == movie.year):
#             raise HTTPException(status_code=409, detail='Фильм с таким названием и годом уже существует')
#         movies_db.append(movie)
#         return movie

from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

class Movie(BaseModel):
    id: int
    title: str
    description: str
    year: Optional[int] = None

# Пример базы данных
movies_db = [
    Movie(id=1, title="Фильм1", description="Описание 1", year=2020),
    Movie(id=2, title="Фильм2", description="Описание 2", year=2022),
    Movie(id=3, title="Фильм3", description="Описание 3", year=2020),
]

@app.get('/movies/', response_model=List[Movie])
def get_movies(
    year: Optional[int] = Query(default=None, description='Год релиза'),
    title: Optional[str] = Query(default=None, description='Название фильма')
):
    results = movies_db
    
    if year is not None:
        results = [movie for movie in results if movie.year == year]
    
    if title is not None:
        # Регистронезависимый поиск
        results = [movie for movie in results 
                  if title.lower() in movie.title.lower()]
    
    return results

@app.get('/movies/{movie_id}', response_model=Movie)
def get_movie_by_id(movie_id: int):
    for movie in movies_db:
        if movie.id == movie_id:
            return movie
    
    raise HTTPException(status_code=404, detail='Movie not found')

@app.post('/movies/', response_model=Movie, status_code=201)
def create_movie(movie: Movie):
    # Проверка 1: уникальность ID
    for m in movies_db:
        if m.id == movie.id:
            raise HTTPException(status_code=400, detail='Фильм с таким ID уже существует')
    
    # Проверка 2: уникальность по названию и году (регистронезависимо)
    for m in movies_db:
        if (m.title.lower() == movie.title.lower() and 
            m.year == movie.year):
            raise HTTPException(status_code=409, detail='Фильм с таким названием и годом уже существует')
    
    # Добавляем фильм ТОЛЬКО после всех проверок
    movies_db.append(movie)
    return movie

# Дополнительно: PUT и DELETE методы
@app.put('/movies/{movie_id}', response_model=Movie)
def update_movie(movie_id: int, updated_movie: Movie):
    for i, movie in enumerate(movies_db):
        if movie.id == movie_id:
            # Проверяем, что новый ID не конфликтует с другими
            if updated_movie.id != movie_id:
                for m in movies_db:
                    if m.id == updated_movie.id and m.id != movie_id:
                        raise HTTPException(status_code=400, detail='ID уже занят другим фильмом')
            
            movies_db[i] = updated_movie
            return updated_movie
    
    raise HTTPException(status_code=404, detail='Movie not found')

@app.delete('/movies/{movie_id}')
def delete_movie(movie_id: int):
    for i, movie in enumerate(movies_db):
        if movie.id == movie_id:
            deleted_movie = movies_db.pop(i)
            return {"message": "Фильм удален", "movie": deleted_movie}
    
    raise HTTPException(status_code=404, detail='Movie not found')
