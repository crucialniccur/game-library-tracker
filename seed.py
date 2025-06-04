#!/usr/bin/env python3

from app.database import get_session
from app.models import User, Library

def seed_data():
    """Add sample data to the database"""
    session = get_session()

    # Clear existing data
    session.query(Library).delete()
    session.query(User).delete()
    session.commit()

    # Create users
    john = User(username="john_doe")
    alice = User(username="alice_smith")
    session.add_all([john, alice])
    session.commit()

    # Create libraries
    libraries = [
        Library(title="PC Games", user=john),
        Library(title="Console Games", user=john),
        Library(title="Mobile Games", user=alice),
        Library(title="Retro Games", user=alice)
    ]
    session.add_all(libraries)
    session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
