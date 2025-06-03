# This file adds some initial data to our database

# Import what we need from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Import our database models
from lib.db.models import Base, User, Library, Game

# Get our database URL from config file
from config import DATABASE_URL

# Create a database engine and create all tables
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Create a Session class and a new session
Session = sessionmaker(bind=engine)
session = Session()

def seed_database():
    """Add some initial data to our database"""
    try:
        # Create two users
        user1 = User(username="john_doe")
        user2 = User(username="jane_smith")
        session.add_all([user1, user2])
        session.commit()  # Save the users to the database

        # Create libraries for our users
        pc_library = Library(title="PC Games", user=user1)
        console_library = Library(title="Console Games", user=user1)
        mobile_library = Library(title="Mobile Games", user=user2)
        session.add_all([pc_library, console_library, mobile_library])
        session.commit()  # Save the libraries to the database

        # Create some games
        games = [
            # Games for PC library
            Game(
                title="The Witcher 3",
                completion_rate=85.5,
                playtime_hours=120.5,
                rating=5,
                library=pc_library
            ),
            Game(
                title="Red Dead Redemption 2",
                completion_rate=92.0,
                playtime_hours=95.0,
                rating=5,
                library=pc_library
            ),
            # Game for console library
            Game(
                title="God of War",
                completion_rate=100.0,
                playtime_hours=45.5,
                rating=5,
                library=console_library
            ),
            # Game for mobile library
            Game(
                title="Monument Valley",
                completion_rate=100.0,
                playtime_hours=3.5,
                rating=4,
                library=mobile_library
            )
        ]
        session.add_all(games)
        session.commit()  # Save the games to the database

        print("Database seeded successfully!")

    except Exception as e:
        # If anything goes wrong, show the error and undo any partial changes
        print(f"Error seeding database: {str(e)}")
        session.rollback()
    finally:
        # Always close the session when we're done
        session.close()

# If this file is run directly (not imported), run the seeding
if __name__ == "__main__":
    seed_database()
