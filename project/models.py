from pydantic import BaseModel, Field
from typing import Optional



class Movie(BaseModel):
    title: str = Field(..., example='Смурфики', description='Movie title')
    year: int = Field(..., example=2011, description='Release year')
    description: str = Field(..., example='Приключения смурфиков в лесу', 
                           description='Movie description')
