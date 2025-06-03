from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    libraries = relationship('Library', back_populates='user', cascade='all, delete')

class Library(Base):
    __tablename__ = 'libraries'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='libraries')
    games = relationship('Game', back_populates='library', cascade='all, delete')

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    library_id = Column(Integer, ForeignKey('libraries.id'))
    library = relationship('Library', back_populates='games')
