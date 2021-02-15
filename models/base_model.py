#!/usr/bin/python3
"""Base model of the console"""
import uuid
from datetime import datetime
import json

class BaseModel:
    """Base Model"""
    
    def __init__(self, *args, **kwargs):
        """Instantion method"""
        now = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = now
        self.updated_at = now

    def __str__(self):
        """Overriding __str__ method"""
        retstr = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        return retstr

    def save(self):
        """Updates updated at attribute"""
        now = datetime.now()
        self.updated_at = now

    def to_dict(self):
        """Returns dict values"""
        book = self.__dict__
        book["__class__"] = self.__class__.__name__
        tmp = book["created_at"]
        book["created_at"] = tmp.isoformat()
        tmp = book["updated_at"]
        book["updated_at"] = tmp.isoformat()
        return book

