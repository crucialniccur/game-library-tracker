from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, User, Library, Game

# Create database and tables
engine = create_engine('sqlite:///game_library.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def seed_database():
    try:
        # Create users
        user1 = User(username="john_doe")
        user2 = User(username="jane_smith")
        session.add_all([user1, user2])
        session.commit()

        # Create libraries
        pc_library = Library(title="PC Games", user=user1)
        console_library = Library(title="Console Games", user=user1)
        mobile_library = Library(title="Mobile Games", user=user2)
        session.add_all([pc_library, console_library, mobile_library])
        session.commit()

        # Add games
        games = [
            Game(
                title="The Witcher 3",
                completion_rate=85.5,
                playtime_hours=120.5,
                rating=10,
                library=pc_library
            ),
            Game(
                title="Red Dead Redemption 2",
                completion_rate=92.0,
                playtime_hours=95.0,
                rating=9,
                library=pc_library
            ),
            Game(
                title="God of War",
                completion_rate=100.0,
                playtime_hours=45.5,
                rating=10,
                library=console_library
            ),
            Game(
                title="Monument Valley",
                completion_rate=100.0,
                playtime_hours=3.5,
                rating=8,
                library=mobile_library
            )
        ]
        session.add_all(games)
        session.commit()

        print("Database seeded successfully!")

    except Exception as e:
        print(f"Error seeding database: {str(e)}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()
