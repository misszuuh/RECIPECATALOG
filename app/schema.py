from pydantic import BaseModel
from typing import Optional

class Restaurant(BaseModel):
    name: str
    ingredients: str
    instructions: str
    prep_time: int
    cooking_time: int
    total_time: Optional[int]

    class Config:
      orm_mode = True