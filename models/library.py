from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base


class Library(Base):
    __tablename__ = 'libraries'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

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

    def get_total_games(self):
        return len(self.games)

    def get_completed_games(self):
        return len([game for game in self.games if game.completed])

    def get_completion_stats(self):
        total = self.get_total_games()
        if total == 0:
            return 0.0
        completed = self.get_completed_games()
        return (completed / total) * 100

    def get_total_play_time(self):
        return sum(game.play_time or 0 for game in self.games)
