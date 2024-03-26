#!/usr/bin/python3
"""
    Create Post
"""


from models.base_model import BaseModel


class Post(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Can be 'facebook', 'twitter', 'linkedin'
        self.platform = kwargs.get('platform', '')  # Assign platform from kwargs or default to empty string
        self.message = kwargs.get('message', '')    # Assign message from kwargs or default to empty string
        # Format: %Y-%m-%dT%H:%M:%S (e.g., 2017-06-14T22:31:03)
        self.schedule_time = kwargs.get('schedule_time', '')  # Assign schedule_time from kwargs or default to empty string
