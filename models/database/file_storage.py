#!/usr/bin/python3
"""
Module for FileStorage class.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects filtered by class name cls."""
        if cls is None:
            return self.__objects
        else:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
    """def all(self):
        ""Returns the dictionary __objects.""
        return self.__objects"""

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key,
                    obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (if the file exists)."""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        if class_name == 'Post':
                            from models.create_post import Post
                            class_instance = Post(**value)
                        else:
                            cls = globals()[class_name]
                            class_instance = cls(**value)
                        self.__objects[key] = class_instance
            except FileNotFoundError:
                pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside."""
        if obj is None:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]

    def get(self, cls, id):
        """Retrieve one object"""
        key = "{}.{}".format(cls.__name__, id)
        return self.__objects.get(key, None)
