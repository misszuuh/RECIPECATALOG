from fastapi import FastAPI,Response,status,HTTPException,Depends, Request, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models,schema, oauth2
from ..database import engine,SessionLocal,get_db


router = APIRouter(
    prefix="/recipes",
    tags=['Recipes']
)



@router.get("/")
def get_recipes(request: Request, db: Session = Depends(get_db),search: Optional[str] = "", user_id: int = Depends(oauth2.get_current_user)):
    recipes = db.query(models.Restaurant).filter(models.Restaurant.name.contains(search)).all()

    return recipes

@router.get("/{id}")
def get_recipe(id: int,db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    recipes = db.query(models.Restaurant).filter(models.Restaurant.id == id).first() 

    if not recipes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"recipes with id: {id} was not found")
       
    return recipes

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_recipes(recipe: schema.Restaurant, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    new_recipe = models.Restaurant(**recipe.dict(), user_id=user_id.id)
    
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)

    return new_recipe
    

@router.put("/{id}")
def update_recipes(id: int, recipe: schema.Restaurant, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
     recipes_query = db.query(models.Restaurant).filter(models.Restaurant.id == id)

     recipes = recipes_query.first()
     if recipes == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"recipes with id: {id} was not found")
     
     recipes_query.update(recipe.dict(), synchronize_session=False)

     db.commit()

     return recipes_query.first()




@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipes(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
     recipes = db.query(models.Restaurant).filter(models.Restaurant.id == id)
     
     if recipes.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} does not exist")
     recipes.delete(synchronize_session=False)

     db.commit() 

    
     return Response(status_code=status.HTTP_204_NO_CONTENT)
     