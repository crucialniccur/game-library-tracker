# fmt: off
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.game import Base
from sqlalchemy import create_engine
# fmt: on

engine = create_engine('sqlite:///db.sqlite3')

Base.metadata.create_all(engine)
print('The database is created with the Tables and Columns innit')
