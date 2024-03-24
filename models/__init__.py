#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.database.file_storage import FileStorage
from models.database.database_db import db
from models.base_model import BaseModel
from models.user import User
from models.analytics_data import AnalyticsData
from models.socialmedia_post import SocialMediaPost
from models.user_profile import UserProfile
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
