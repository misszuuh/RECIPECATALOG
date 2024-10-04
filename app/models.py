from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

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
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False) 
    owner = relationship("User")  





class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False) 
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))   