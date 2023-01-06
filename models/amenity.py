#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place, place_amenity


'''place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))'''


class Amenity(BaseModel, Base):
    """
    Python model representation of `amenities` in database
    Attributes:
        __tablename__: represents the table name, amenities
        name: represents a column containing a string
        place_amenities: represent a relationship Many-To-Many
        between the class Place and Amenity
    """
    __tablename__ = "amenities"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity,
                                       back_populates='amenities')
    else:
        name = ''
