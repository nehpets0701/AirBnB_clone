#!/usr/bin/python3
"""Base model of the console"""
import uuid
from datetime import datetime

class BaseModel:
    """Base Model"""
    
    def __init__(self, id=None, created_at=None, updated_at=None):
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
