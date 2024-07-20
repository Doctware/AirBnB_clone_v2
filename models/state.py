#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """ iheriting from BaseModel """
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """
        Getter
        this method returns the list of City instances with
        state_id equls to the current State.id => it will be the file storage
        relationship between state and city
        """

        city_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
