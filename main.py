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


def delete_game(game_id):
    game = session.query(Game).get(game_id)
    if game:
        session.delete(game)
        session.commit()
        print(f'Deleted succesfully innit')
    else:
        print(f'No game found with id {game_id}')
