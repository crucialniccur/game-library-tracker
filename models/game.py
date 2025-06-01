from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    platform = Column(String)
    completed = Column(Boolean, default=False)
    rating = Column(Integer)
    play_time = Column(Integer, default=0)  # in minutes
    last_played = Column(DateTime)
    library_id = Column(Integer, ForeignKey('libraries.id'))

    # Relationship
    library = relationship("Library", back_populates="games")

    def __repr__(self):
        return f"<Game(id={self.id}, title='{self.title}', platform='{self.platform}', completed={self.completed})>"

    def mark_as_played(self, minutes=0):
        self.last_played = datetime.now()
        self.play_time += minutes

    def toggle_completion(self):
        # Get the current value from the database
        current_completed = bool(self.completed)
        # Toggle it
        self.completed = not current_completed
        return self.completed
