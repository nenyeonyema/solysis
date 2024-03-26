#!/usr/bin/python3
"""
Module for SocialMediaPost class.
"""
from models.base_model import BaseModel

class SocialMediaPost(BaseModel):
    """
    SocialMediaPost class representing a social media post.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of SocialMediaPost.
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id', "")
        self.platform = kwargs.get('platform', "")
        self.message = kwargs.get('message', "")
        self.schedule_time = kwargs.get('schedule_time', "")
        self.likes = kwargs.get('likes', 0)
        self.views = kwargs.get('views', 0)
        self.comments = kwargs.get('comments', 0)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        obj_dict = super().to_dict()
        obj_dict['user_id'] = self.user_id
        obj_dict['platform'] = self.platform
        obj_dict['message'] = self.message
        obj_dict['schedule_time'] = self.schedule_time
        obj_dict['likes'] = self.likes
        obj_dict['views'] = self.views
        obj_dict['comments'] = self.comments
        return obj_dict

    def __str__(self):
        """
        Returns the string representation of the SocialMediaPost.
        """
        return "[{}] ({}) User: {} - Platform: {} - Message: {}".format(
            self.__class__.__name__, self.id, self.user_id, self.platform, self.message)
