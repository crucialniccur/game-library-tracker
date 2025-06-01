from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base


class Library(Base):
    __tablename__ = 'libraries'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)

    # Relationships
    user = relationship("User", back_populates="libraries")
    games = relationship("Game", back_populates="library", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Library(id={self.id}, title='{self.title}', user_id={self.user_id})>"

    def add_game(self, game):
        self.games.append(game)

    def remove_game(self, game):
        if game in self.games:
            self.games.remove(game)

    def get_completion_stats(self):
        if not self.games:
            return 0
        completed = sum(1 for game in self.games if game.completed)
        return (completed / len(self.games)) * 100
