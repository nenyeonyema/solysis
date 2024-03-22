#!/usr/bin/python3
"""
User
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from models.base_model import BaseModel
from models.engine.database import db


Base = declarative_base()


class User(BaseModel, Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'
