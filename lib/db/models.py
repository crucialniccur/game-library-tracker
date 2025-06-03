from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    """
    User Model - The parent in one-to-many relationship with Libraries
    One User can have Many Libraries
    """
    __tablename__ = 'users'

    # Primary Key
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)

    # One-to-Many: One User has Many Libraries
    # When a user is deleted, all their libraries will be deleted (cascade)
    libraries = relationship('Library', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.username}>"

class Library(Base):
    """
    Library Model
    - Child in one-to-many with User (Many Libraries belong to One User)
    - Parent in one-to-many with Games (One Library has Many Games)
    """
    __tablename__ = 'libraries'

    # Primary Key
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    # Foreign Key for One-to-Many with User
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    # Relationships
    # Many-to-One: Many Libraries belong to One User
    user = relationship('User', back_populates='libraries')
    # One-to-Many: One Library has Many Games
    # When a library is deleted, all its games will be deleted (cascade)
    games = relationship('Game', back_populates='library', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Library {self.title}>"

class Game(Base):
    """
    Game Model - The child in one-to-many relationship with Library
    Many Games belong to One Library
    """
    __tablename__ = 'games'

    # Primary Key
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    completion_rate = Column(Float, default=0)
    playtime_hours = Column(Float, default=0)
    rating = Column(Integer)

    # Foreign Key for One-to-Many with Library
    library_id = Column(Integer, ForeignKey('libraries.id'), nullable=False)

    # Many-to-One: Many Games belong to One Library
    library = relationship('Library', back_populates='games')

    def __repr__(self):
        return f"<Game {self.title}>"
