from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Use SQLite for simplicity
DATABASE_URL = "sqlite:///game_library.db"

# Create engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
