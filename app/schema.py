from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class Restaurant(BaseModel):
    name: str
    ingredients: str
    instructions: str
    prep_time: int
    cooking_time: int
    total_time: Optional[int]

    class Config:
      orm_mode = True


class RecipeCreate(Restaurant):
  pass

class UserOut(BaseModel):
   id: int
   email: EmailStr
   created_at: datetime



class Recipe(Restaurant):
   id: int
   created_at: datetime
   user_id: int
   owner: UserOut 

   class Config:
      orm_mode = True
     


class UserCreate(BaseModel):
   email: EmailStr
   password: str 



class UserLogin(BaseModel):
   email: EmailStr
   password: str

class Token(BaseModel):
   access_token: str
   token_type: str

class TokenData(BaseModel):
   id: Optional[int] = None
   