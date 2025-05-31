from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    platform = Column(String)
    completed = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Game(id={self.id}, title='{self.title}', completed={self.completed})>"
