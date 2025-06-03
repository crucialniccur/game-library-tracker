from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, User, Library, Game
import ipdb

def debug_session():
    """Create a debug session with database access"""
    engine = create_engine('sqlite:///game_library.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("\nDebug session started!")
    print("Available models: User, Library, Game")
    print("Session available as 'session'")
    print("\nExample queries:")
    print("session.query(User).all()")
    print("session.query(Library).first()")
    print("session.query(Game).filter_by(title='The Witcher 3').first()")

    ipdb.set_trace()
