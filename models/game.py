from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    play_time = Column(Integer, default=0)
    rating = Column(Integer)
    library_id = Column(Integer, ForeignKey('libraries.id'))

    # Relationship
    library = relationship("Library", back_populates="games")

    def __repr__(self):
        return f"<Game(id={self.id}, title='{self.title}', platform='{self.platform}', completed={self.completed})>"

    def mark_as_played(self, minutes):
        if not isinstance(minutes, int) or minutes < 0:
            raise ValueError("Play time must be a positive integer")
        self.play_time = (self.play_time or 0) + minutes

    def toggle_completion(self):
        self.completed = not self.completed
        return self.completed
