from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # Relationships
    libraries = relationship("Library", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

    def get_total_games(self):
        return sum(len(library.games) for library in self.libraries)

    def get_total_play_time(self):
        total = 0
        for library in self.libraries:
            for game in library.games:
                total += game.play_time or 0
        return total
