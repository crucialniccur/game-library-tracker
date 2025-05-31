from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    libraries = relationship("Library", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
