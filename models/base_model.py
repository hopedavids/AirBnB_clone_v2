#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from models import storage
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime


Base = declarative_base()
class BaseModel:
    """A base class for all hbnb models"""
    id = Column(Integer, nullable=False,  primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated = Column(DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                if k != "__class__":
                    setattr(self, k, v)
            if "id" not in kwargs:
                setattr(self, "id", str(uuid.uuid4()))
            time = datetime.utcnow()
            if "created_at" not in kwargs:
                setattr(self, "created_at", time)
            if "updated_at" not in kwargs:
                setattr(self, "updated_at", time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            from models import storage
            storage.new(self)
  

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        from models import storage
        storage.save()

        

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)


    def delete(self):
        storage.delete(self)


    def to_dict(self):
        """Converts instance into dictionary format"""
        dictionary = self.__dict__.copy()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['__class__'] = type(self).__name__
        return dictionary

