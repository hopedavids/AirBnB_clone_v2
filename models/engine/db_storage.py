#!/usr/bin/python3
""" DB module for HBNB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv


class DBStorage:
    __engine = None
    __sessions = None

    def __init__(self):
        '''Create engine and sessions '''
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')


        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

        def all(self, cls=None):

            """ Query all objects depending of the class name """
            objs = {}
            if cls:
                query = self.__session.query(cls).all()
                for obj in query:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objs[key] = obj
            else:
                classes = [User, State, City, Amenity, Place, Review]
                for cls in classes:
                    query = self.__session.query(cls).all()
                    for obj in query:
                        key = obj.__class__.__name__ + '.' + obj.id
                        objs[key] = obj
            return objs

        def new(self, obj):
            """Add the object to the database"""
            self.__session.add(obj)

        def save(self):
            """Commit all changes of the current session"""
            self.__session.commit()

        def delete(self, obj=None):
            """Delete from the current database session obj if not None"""
            if obj:
                self.__session.delete(obj)

        def reload(self):
            """Create all tables in the database"""
            Base.metadata.create_all(bind=self.__engine)
            Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
            self.__session = Session()
