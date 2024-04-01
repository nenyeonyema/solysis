#!/usr/bin/python3
"""
User
"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


class User(BaseModel, Base):
    """
    User class representing a user entity.
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    username = Column(String(50))
    location = Column(String(50))
    age = Column(Integer)
    gender = Column(String(20))

