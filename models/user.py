#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """Python model representation of a `User` table
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
        places: constraint to delete a Place instance if its
                corresponding User instance is deleted.
        reviews: constraint to delete a Review instance if its
                corresponding User instance is deleted.

    """
    __tablename__ = "users"
    '''email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place",
                          cascade="all, delete, delete-orphan",
                          backref="user")
    reviews = relationship("Review",
                           cascade="all, delete, delete-orphan",
                           backref="user")'''

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place",
                              cascade="all, delete, delete-orphan",
                              backref="user")
        reviews = relationship("Review",
                               cascade="all, delete, delete-orphan",
                               backref="user")

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
