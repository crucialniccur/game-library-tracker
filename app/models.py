from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    libraries = relationship('Library', back_populates='user', cascade='all, delete')

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"

class Library(Base):
    __tablename__ = 'libraries'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='libraries')

    def __repr__(self):
        return f"<Library(id={self.id}, title='{self.title}', user_id={self.user_id})>"
