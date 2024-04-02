#!/usr/bin/python3
"""
    This module instantiates an object of class FileStorage
"""
from models.base_model import BaseModel
from models.user import User
from models.create_post import Post
from models.socialmedia_post import SocialMediaPost
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.database.database_db import DBStorage
    storage = DBStorage()
else:
    from models.database.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
