#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, values
from sqlalchemy.orm import relationship

from models.review import Review


class Place(BaseModel, Base):
    """Python model representation of a `Place` database
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
        if `db` is selected:
            reviews: constraint to delete a Review instance if its
            corresponding Place instance is deleted.
        else:
            reviews: a list of reviews

    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review",
                               cascade='all, delete, delete-orphan',
                               backref="place")

    else:
        @property
        def reviews(self):
            """returns a list of Review instances"""
            from models import storage
            review_list = []
            reviews_dict = storage.all(Review)
            for inst in reviews_dict.values():
                if self.id == inst.place_id:
                    review_list.append(inst)
            return review_list
