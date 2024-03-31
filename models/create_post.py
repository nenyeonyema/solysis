#!/usr/bin/python3
"""
    Create Post
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


class Post(BaseModel, Base):
    """
    Post class representing a post entity.
    """
    __tablename__ = 'posts'

    platform = Column(String(128), nullable=False)
    message = Column(String(255), nullable=False)
    schedule_time = Column(String(20), nullable=True)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of Post.
        """
        super().__init__(*args, **kwargs)
