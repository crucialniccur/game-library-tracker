from sqlalchemy import create_engine
from models.game import Base

engine = create_engine('sqlite:///games.db')

Base.metadata.create_all(engine)
print('The database is created with the Tables and Columns innit')
