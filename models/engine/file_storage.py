#!/usr/bin/python3
"""Defines the file storae class."""
from models.base_models import BaseModel
import json


class FileStorage:
    """File storage class."""
    __file_path = "file json"
    __objects = {}

    def all(self):
        """Returns store objects."""
        return self.__objects

    def new(self, obj):
        """Stores new object."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON file."""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes JSON files to objects."""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
