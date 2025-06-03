# This file helps set up our database connection

# Import what we need from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import our database models
from models.game import Base

# Get our database URL from config file
from config import DATABASE_URL

# Create a database engine - this is what SQLAlchemy uses to talk to the database
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class - we use this to create database sessions
# A session is like a conversation with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Create all database tables"""
    # This creates all tables defined in our models
    Base.metadata.create_all(bind=engine)
