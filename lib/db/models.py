from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    """
    User Model - Can have many libraries
    Example: john_gamer can have PC Games and Console Games libraries
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    libraries = relationship('Library', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.username}>"

class Library(Base):
    """
    Library Model - Belongs to one user and can have many games
    Example: PC Games library belongs to john_gamer and contains multiple games
    """
    __tablename__ = 'libraries'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='libraries')
    games = relationship('Game', back_populates='library', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Library {self.title}>"

class Game(Base):
    """
    Game Model - Belongs to one library
    Example: 'The Witcher 3' belongs to PC Games library
    """
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    library_id = Column(Integer, ForeignKey('libraries.id'), nullable=False)

    library = relationship('Library', back_populates='games')

    def __repr__(self):
        return f"<Game {self.title}>"
