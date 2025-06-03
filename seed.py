#!/usr/bin/env python3

from app.database import get_session
from app.models import User, Library, Game

def seed_data():
    """Add sample data to the database"""
    session = get_session()

    # Clear existing data
    session.query(Game).delete()
    session.query(Library).delete()
    session.query(User).delete()
    session.commit()

    # Create users
    john = User(username="john_doe")
    alice = User(username="alice_smith")
    session.add_all([john, alice])
    session.commit()

    # Create libraries
    pc_lib = Library(title="PC Games", user=john)
    console_lib = Library(title="Console Games", user=john)
    mobile_lib = Library(title="Mobile Games", user=alice)
    session.add_all([pc_lib, console_lib, mobile_lib])
    session.commit()

    # Add games
    games = [
        Game(title="The Witcher 3", library=pc_lib),
        Game(title="Cyberpunk 2077", library=pc_lib),
        Game(title="God of War", library=console_lib),
        Game(title="Pokemon GO", library=mobile_lib)
    ]
    session.add_all(games)
    session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
