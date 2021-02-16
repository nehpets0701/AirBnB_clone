#!/usr/bin/python3
"""Base model of the console"""
import uuid
from datetime import datetime
import json

class BaseModel:
    """Base Model"""
    
    def __init__(self, *args, **kwargs):
        """Instantion method"""
        if len(kwargs) != 0:
            """Create instance"""
            for key, value in kwargs.items():
                if key == '__class__':
                    setattr(self, key, type(self))
                elif key == 'created_at' or key == 'updated_at':
                    """Formats datetime"""
                    setattr(self, key, datetime.strptime(value,  "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            """No dict create new instance"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models.__init__ import storage
            storage.new(self)
    
    def __str__(self):
        """Overriding __str__ method"""
        retstr = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        return retstr

    def save(self):
        """Updates updated at attribute"""
        now = datetime.now()
        self.updated_at = now
        from models.__init__ import storage
        storage.save()
    
    def to_dict(self):
        """Returns dictionary instance attributes"""
        attributes = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                attributes[key] = value.isoformat()
            else:
                attributes[key] = value
        attributes['__class__'] = type(self).__name__
        return attributes
