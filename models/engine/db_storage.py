#!/usr/bin/python3
""" The Dtatbase Stroge """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os
from models import storage


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
        if cls is None:
            objs = {}
            for class_name, class_type in storage.classes.items():
                for obj in self.__session.quary(class_type).all():
                    key = f"{class_name}.{obj.id}"
                    objs[key] = obj
            return objs
        else:
            objs = {}
            for obj in self.__session.quary(cls).all():
                key = f"{cls.__name__}.{obj.id}"
                objs[key] = obj
            return objs

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

        Base.metadate.create_all(self.__engine)
        session_factory =\
            sessionmaker(bind=self.__engine, expire_on_cimmit=False)
        self.__engine = scoped_session(session_factory)
