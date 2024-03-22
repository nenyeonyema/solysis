#!/usr/bin/python3
"""
Analytic Data
"""
from models.engine.database import db


class AnalyticsData(db.Model):
    __tablename__ = 'analytics_data'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('social_media_posts.id'), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Integer, nullable=False)
    shares = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)
    # Add other fields as needed for engagement metrics and demographics
