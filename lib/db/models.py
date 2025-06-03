from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    """
    User Model - The parent in one-to-many relationship with Libraries
    One User can have Many Libraries
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)

    # One-to-Many: One User has Many Libraries
    libraries = relationship('Library', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.username}>"

class Library(Base):
    """
    Library Model - The child in one-to-many relationship with User
    Many Libraries belong to One User
    """
    __tablename__ = 'libraries'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    # Many-to-One: Many Libraries belong to One User
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='libraries')

    def __repr__(self):
        return f"<Library {self.title}>"
