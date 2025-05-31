from models.game import Game, session
import argparse


def add_game(title, genre, platform):
    game = Game(title=title, genre=genre, platform=platform)
    session.add(game)
    session.commit()
    print('Game : --{game}-- added succesfully')


def list_games():
    games = session.query(Game).all()
    for game in games:
        print(game)
