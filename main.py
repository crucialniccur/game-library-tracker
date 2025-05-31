from models.game import Game, session
import argparse


def add_game(title, genre, platform):
    game = Game(title=title, genre=genre, platform=platform)
    session.add(game)
    session.commit()
    print(f'Game : --{game}-- added succesfully')


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


def main():
    parser = argparse.ArgumentParser(description="Manage your game library")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--title", required=True)
    add_parser.add_argument("--genre", required=True)
    add_parser.add_argument("--platform", required=True)

    list_parser = subparsers.add_parser("list")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)

    args = parser.parse_args()

    if args.command == "add":
        add_game(args.title, args.genre, args.platform)
    elif args.command == "list":
        list_games()
    elif args.command == "delete":
        delete_game(args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
