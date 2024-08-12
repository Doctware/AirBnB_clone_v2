#!/usr/bin/python3
""" The Dtatbase Stroge """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
import os
import models

from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ The class Database Storage """
    __engine = None
    __session = None

    def __init__(self):
        """ the Init method """

        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{database}",
            pool_pre_ping=True
        )

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        self.__session = scoped_session\
            (sessionmaker(bind=self.__engine, expire_on_commit=False))

    def all(self, cls=None):
        """ Query on the current session self.__session """
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(State, City).all()
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in objs}

    def new(self, obj):
        """ method thats adds objects to the current database sessions """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ this method commit all changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ this method delete from the current database session """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ This method create all tables in the Database """

        Base.metadata.create_all(self.__engine)
        session_factory =\
            sessionmaker(bind=self.__engine, expire_on_cimmit=False)
        self.__engine = scoped_session(session_factory)

    def close(self):
        """ this method diserialized obj to json """
        self.__session.remove()
