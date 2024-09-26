from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class Restaurant(Base):
    __tablename__="recipes"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)
    instructions = Column(String, nullable=False)
    prep_time = Column(Integer,nullable=False)
    cooking_time = Column(Integer,nullable=False)
    total_time = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=('now()'))   
