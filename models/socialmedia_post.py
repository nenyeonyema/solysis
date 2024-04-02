#!/usr/bin/python3
"""
Module for SocialMediaPost class.
"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer


class SocialMediaPost(BaseModel, Base):
    """
    SocialMediaPost class representing a social media post.
    """
    __tablename__ = 'social_media_posts'


    user_id = Column(String(60), nullable=False)
    platform = Column(String(128), nullable=False)
    message = Column(String(255), nullable=False)
    schedule_time = Column(String(20), nullable=True)
    """likes = Column(Integer, nullable=False, default=0)
    views = Column(Integer, nullable=False, default=0)
    comments = Column(Integer, nullable=False, default=0)"""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of SocialMediaPost.
        """
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        obj_dict = super().to_dict()
        obj_dict['user_id'] = self.user_id
        obj_dict['platform'] = self.platform
        obj_dict['message'] = self.message
        obj_dict['schedule_time'] = self.schedule_time
        """obj_dict['likes'] = self.likes
        obj_dict['views'] = self.views
        obj_dict['comments'] = self.comments"""
        return obj_dict

    def __str__(self):
        """
        Returns the string representation of the SocialMediaPost.
        """
        return "[{}] ({}) User: {} - Platform: {} - Message: {}".format(
            self.__class__.__name__, self.id, self.user_id, self.platform, self.message)
