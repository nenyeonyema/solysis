#!/usr/bin/python3
"""
    This module instantiates an object of class FileStorage
"""
from models.database.file_storage import FileStorage
from models.database.database_db import db
from models.base_model import BaseModel
from models.user import User
from models.create_post import Post
from models.socialmedia_post import SocialMediaPost
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
