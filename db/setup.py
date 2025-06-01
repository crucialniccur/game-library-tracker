from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.game import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///db/game_library.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
