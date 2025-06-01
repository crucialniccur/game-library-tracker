import argparse
from db.session import SessionLocal
from models import User, Library, Game

db = SessionLocal()
parser = argparse.ArgumentParser(description='🎮 Game Library Tracker CLI')
subparsers = parser.add_subparsers(dest='command')

# ----- User Commands -----
add_user_parser = subparsers.add_parser('add-user')
add_user_parser.add_argument('name', help='User name')

list_users_parser = subparsers.add_parser('list-users')

# ----- Library Commands -----
add_lib_parser = subparsers.add_parser('add-library')
add_lib_parser.add_argument('title', help='Library title')
add_lib_parser.add_argument('user_id', type=int, help='User ID')

list_libs_parser = subparsers.add_parser('list-libraries')

# ----- Game Commands -----
add_game_parser = subparsers.add_parser('add-game')
add_game_parser.add_argument('title', help='Game title')
add_game_parser.add_argument('genre', help='Game genre')
add_game_parser.add_argument('platform', help='Game platform')
add_game_parser.add_argument('library_id', type=int, help='Library ID')

list_games_parser = subparsers.add_parser('list-games')

delete_game_parser = subparsers.add_parser('delete-game')
delete_game_parser.add_argument('id', type=int, help='Game ID')

# ----- Execution -----
args = parser.parse_args()

if args.command == 'add-user':
    user = User(name=args.name)
    db.add(user)
    db.commit()
    print(f"✅ Added user: {user.name}")

elif args.command == 'list-users':
    users = db.query(User).all()
    for user in users:
        print(f"👤 {user.id}: {user.name}")

elif args.command == 'add-library':
    lib = Library(title=args.title, user_id=args.user_id)
    db.add(lib)
    db.commit()
    print(f"📚 Added library: {lib.title} for user ID {args.user_id}")

elif args.command == 'list-libraries':
    libraries = db.query(Library).all()
    for lib in libraries:
        print(f"📘 {lib.id}: {lib.title} (User {lib.user_id})")

elif args.command == 'add-game':
    game = Game(title=args.title, genre=args.genre,
                platform=args.platform, library_id=args.library_id)
    db.add(game)
    db.commit()
    print(
        f"🎮 Game added: {game.title} | Genre: {game.genre} | Platform: {game.platform}")

elif args.command == 'list-games':
    games = db.query(Game).all()
    for g in games:
        print(
            f"🎲 {g.id}: {g.title} - {g.genre} on {g.platform} (Library ID {g.library_id})")

elif args.command == 'delete-game':
    game = db.get(Game, args.id)
    if game:
        db.delete(game)
        db.commit()
        print(f"🗑️ Deleted game ID {args.id}")
    else:
        print(f"❌ No game found with ID {args.id}")

else:
    parser.print_help()
