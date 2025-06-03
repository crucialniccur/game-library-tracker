from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)

    # Relationships
    libraries = relationship("Library", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"

    def get_total_games(self):
        return sum(len(library.games) for library in self.libraries)

    def get_completed_games(self):
        return sum(len([game for game in library.games if game.completion_rate == 100]) for library in self.libraries)

    def get_completion_rate(self):
        total = self.get_total_games()
        if total == 0:
            return 0.0
        return (self.get_completed_games() / total) * 100

    def get_total_play_time(self):
        total = 0
        for library in self.libraries:
            for game in library.games:
                total += game.playtime_hours or 0
        return total
