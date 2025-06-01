from db.session import get_db
from models.user import User
from models.library import Library
from models.game import Game
from datetime import datetime

def seed_database():
    db = next(get_db())

    # Create users
    john = User(name="John Doe")
    jane = User(name="Jane Smith")
    db.add_all([john, jane])
    db.commit()

    # Create libraries
    pc_lib = Library(title="PC Games", user_id=john.id)
    console_lib = Library(title="Console Games", user_id=john.id)
    mobile_lib = Library(title="Mobile Games", user_id=jane.id)
    db.add_all([pc_lib, console_lib, mobile_lib])
    db.commit()

    # Create games
    games = [
        Game(
            title="The Witcher 3",
            genre="RPG",
            platform="PC",
            rating=5,
            library_id=pc_lib.id
        ),
        Game(
            title="Red Dead Redemption 2",
            genre="Action",
            platform="PS4",
            rating=5,
            library_id=console_lib.id
        ),
        Game(
            title="Monument Valley",
            genre="Puzzle",
            platform="iOS",
            rating=4,
            library_id=mobile_lib.id,
            completed=True,
            play_time=120,
            last_played=datetime.now()
        )
    ]
    db.add_all(games)
    db.commit()

    print("Database seeded!")

if __name__ == "__main__":
    seed_database()
