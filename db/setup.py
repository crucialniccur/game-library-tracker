from sqlalchemy import create_engine
from models.game import Base

engine = create_engine('sqlite:///games.db')
