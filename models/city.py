#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ Model representation of `citiy` table
    Attributes:
        state_id: The state id
        name: input name
        places: constraint to delete a Place instance if its
                corresponding City instance is deleted.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place",
                          cascade='all, delete, delete-orphan',
                          backref="cities")
