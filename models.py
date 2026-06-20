from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, default="")
    completed = Column(Boolean, default=False)

class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,index=True)
    description = Column(String, default="")
    completed = Column(Boolean, default=False)

class User(Base):
    __tablename__ ="user"

    id = Column(Integer, primary_key=True, index=True)
    hashed_password =Column(String)