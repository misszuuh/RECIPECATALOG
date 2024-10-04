from fastapi import FastAPI,Response,status,HTTPException,Depends, Request
from . import models,schema
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from .database import engine,SessionLocal,get_db
from typing import List
from .routers import recipe, user, auth


models.Base.metadata.create_all(bind=engine)


app = FastAPI()



app.include_router(recipe.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return{"message": "Welcome to my api."}


while True:

    try:
        conn = psycopg2.connect(host='localhost', database='catalog', user='postgres',
        password='zubeda', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succcessfully!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)  
        time.sleep(2)  


