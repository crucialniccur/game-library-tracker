from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base


class Library(Base):
    __tablename__ = 'libraries'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    game_id = Column(Integer, ForeignKey('games.id'))

    user = relationship("User", back_populates="libraries")

    def __repr__(self):
        return f"<Library(user_id={self.user_id}, game_id={self.game_id})>"
