#!/usr/bin/python3
"""
Social Media post class
"""
from datetime import datetime
from models.engine.database import db


class SocialMediaPost(db.Model):
    __tablename__ = 'social_media_posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<SocialMediaPost {self.id}>'
