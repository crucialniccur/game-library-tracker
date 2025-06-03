# This file handles database connections

# Import what we need from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Get our database URL from config file
from config import DATABASE_URL

# Create a database engine with SQLite-specific settings
# check_same_thread=False allows us to use SQLite with multiple threads
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Only needed for SQLite
)

# Create a SessionLocal class - we use this to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Get a database session

    This function:
    1. Creates a new database session
    2. Makes sure the session is closed after we're done
    3. Returns the session so we can use it
    """
    # Create a new session
    db = SessionLocal()
    try:
        # Give the session to whoever called this function
        yield db
    finally:
        # Make sure to close the session when we're done
        db.close()
