#!/usr/bin/python3
"""
Contains class BaseModel
"""
from datetime import datetime
from models.engine.database import db

class BaseModel:
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        from models.engine.database import db
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        from models.engine.database import db
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
            # Include additional common attributes as needed
        }
