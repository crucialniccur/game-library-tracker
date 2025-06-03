from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    libraries = relationship('Library', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.username}>"

class Library(Base):
    __tablename__ = 'libraries'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='libraries')
    games = relationship('Game', back_populates='library', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Library {self.name}>"

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    completion_rate = Column(Float, default=0)
    playtime_hours = Column(Float, default=0)
    rating = Column(Integer)
    library_id = Column(Integer, ForeignKey('libraries.id'), nullable=False)
    library = relationship('Library', back_populates='games')

    def __repr__(self):
        return f"<Game {self.title}>"
