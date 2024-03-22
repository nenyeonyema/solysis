#!/usr/bin/python3
"""
Contains the class DBStorage
"""
from flask_sqlalchemy import SQLAlchemy
import models
# from models.user import User

db = SQLAlchemy()

def init_app(app):
    from models.user import User
    from models.base_model import db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///solysis.db'
    db.init_app(app)
