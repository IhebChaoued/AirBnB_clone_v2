#!/usr/bin/python3
"""Defines a class for file storage management in the hbnb clone"""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Manages database storage"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize database storage"""
        hb_user = getenv("HBNB_MYSQL_USER")
        hb_pwd = getenv("HBNB_MYSQL_PWD")
        hb_host = getenv("HBNB_MYSQL_HOST")
        hb_db = getenv("HBNB_MYSQL_DB")
        hb_env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{hb_user}:{hb_pwd}@{hb_host}/{hb_db}",
            pool_pre_ping=True,
        )

        if hb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """Reload database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()

    def all(self, cls=None, id=None):
        """Query all classes or specific one by ID"""
        allClasses = [User, Place, State, City, Amenity, Review]
        result = {}

        if cls is not None:
            if id is not None:
                obj = self.__session.query(cls).get(id)
                if obj is not None:
                    ClassName = obj.__class__.__name__
                    keyName = ClassName + "." + str(obj.id)
                    result[keyName] = obj
            else:
                for obj in self.__session.query(cls).all():
                    ClassName = obj.__class__.__name__
                    keyName = ClassName + "." + str(obj.id)
                    result[keyName] = obj
        else:
            for clss in allClasses:
                if id is not None:
                    obj = self.__session.query(clss).get(id)
                    if obj is not None:
                        ClassName = obj.__class__.__name__
                        keyName = ClassName + "." + str(obj.id)
                        result[keyName] = obj
                else:
                    for obj in self.__session.query(clss).all():
                        ClassName = obj.__class__.__name__
                        keyName = ClassName + "." + str(obj.id)
                        result[keyName] = obj
        return result

    def search(self, cls, id):
        """Search method"""
        data = self.all(cls)

    def new(self, obj):
        """Add new object to the session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes to the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the session"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """Close the session"""
        self.__session.close()
