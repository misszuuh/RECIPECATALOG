from fastapi import FastAPI,Response,status,HTTPException,Depends, Request
from . import models,schema
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from .database import engine,SessionLocal,get_db
from typing import List


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
def root():
    return{"message": "Welcome to my api."}

@app.get("/recipes")
def get_recipes(request: Request, db: Session = Depends(get_db)):
    cooking_time = request.query_params.get("cooking_time")
    name = request.query_params.get("name")
    recipes = db.query(models.Restaurant)

    if cooking_time != None:
        recipes = recipes.filter(models.Restaurant.cooking_time == cooking_time)

    if name != None:
        recipes = recipes.filter(models.Restaurant.name == name)
        
    recipes = recipes.all()

    for r in recipes:
        r.total_time = r.cooking_time + r.prep_time
    return recipes

@app.get("/recipes/{id}")
def get_recipes(id: int,db: Session = Depends(get_db)):
    recipes = db.query(models.Restaurant).filter(models.Restaurant.id == id).first() 

    if not recipes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"recipes with id: {id} was not found")
       
    return recipes

@app.post("/recipes",status_code=status.HTTP_201_CREATED)
def create_recipes(recipe: schema.Restaurant, db: Session = Depends(get_db)):
    new_recipe = models.Restaurant(**recipe.dict())
    
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)

    return {"data":new_recipe}
    

@app.put("/recipes/{id}")
def update_recipes(id: int, recipe: schema.Restaurant, db: Session = Depends(get_db)):
     recipes_query = db.query(models.Restaurant).filter(models.Restaurant.id == id)

     recipes = recipes_query.first()
     if recipes == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"recipes with id: {id} was not found")
     
     recipes_query.update(recipe.dict(), synchronize_session=False)

     db.commit()

     return recipes_query.first()




@app.delete("/recipes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipes(id: int, db: Session = Depends(get_db)):
     recipes = db.query(models.Restaurant).filter(models.Restaurant.id == id)
     
     if recipes.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} does not exist")
     recipes.delete(synchronize_session=False)

     db.commit() 

    
     return Response(status_code=status.HTTP_204_NO_CONTENT)
     

#@app.get("/recipes/")
#def filter_recipes_by_time(total_time: int, db: Session = Depends(get_db)) -> List[models.Restaurant]:
    # Calculate total time (prep_time + cooking_time) and filter based on the provided total_time
    #filtered_recipes = db.query(models.Restaurant).filter((models.Restaurant.prep_time + models.Restaurant.cooking_time)
                               # <= total_time).all()

   # if not filtered_recipes:
        #raise HTTPException(status_code=404, detail="No recipes found with the given total time")

    #return filtered_recipes





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


