from models.game import Game
from db.session import session


def seed_data():
    games = [
        Game(title="The Legend of Zelda: Breath of the Wild",
             genre="Adventure", platform="Nintendo Switch"),
        Game(title="God of War", genre="Action", platform="PS4"),
        Game(title="Stardew Valley", genre="Simulation", platform="PC"),
        Game(title="Hades", genre="Roguelike", platform="PC"),
        Game(title="Hollow Knight", genre="Metroidvania", platform="PC"),
    ]

    session.add_all(games)
    session.commit()
    print("Seeding sseeded with dummy games!")


if __name__ == "__main__":
    seed_data()
