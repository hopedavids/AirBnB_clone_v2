#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, CHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel):
    """ The city class, contains state ID and name """
    
    __tablename__ = 'city'

    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', String(60), ForeignKey('state_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(*args, **kwargs)

