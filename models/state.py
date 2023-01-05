#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """return a list of city instances"""
        from models import storage
        city_list = []
        cities_dict = storage.all(City)
        for inst in cities_dict.values():
            if self.id == inst.state_id:
                city_list.append(inst)
        return city_list
