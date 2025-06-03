from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Create database engine
engine = create_engine('sqlite:///game_library.db')

# Create all tables
Base.metadata.create_all(engine)

# Create session factory
Session = sessionmaker(bind=engine)

def get_session():
    """Get a new database session"""
    return Session()
