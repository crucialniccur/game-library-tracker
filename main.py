import argparse
from datetime import datetime
from sqlalchemy.orm import Session
from db.session import get_db
from models.user import User
from models.library import Library
from models.game import Game

db = next(get_db())
parser = argparse.ArgumentParser(description='🎮 Game Library Tracker CLI')
subparsers = parser.add_subparsers(dest='command')

# ----- User Commands -----
add_user_parser = subparsers.add_parser('add-user', help='Add a new user')
add_user_parser.add_argument('name', help='User name')

list_users_parser = subparsers.add_parser('list-users', help='List all users')

# ----- Library Commands -----
add_lib_parser = subparsers.add_parser('add-library', help='Add a new library')
add_lib_parser.add_argument('title', help='Library title')
add_lib_parser.add_argument('user_id', type=int, help='User ID')

list_libs_parser = subparsers.add_parser('list-libraries', help='List all libraries')
list_libs_parser.add_argument('--user-id', type=int, help='Filter by user ID')

# ----- Game Commands -----
add_game_parser = subparsers.add_parser('add-game', help='Add a new game')
add_game_parser.add_argument('title', help='Game title')
add_game_parser.add_argument('genre', help='Game genre')
add_game_parser.add_argument('platform', help='Game platform')
add_game_parser.add_argument('library_id', type=int, help='Library ID')
add_game_parser.add_argument('--rating', type=int, choices=range(1, 6), help='Game rating (1-5)')

list_games_parser = subparsers.add_parser('list-games', help='List all games')
list_games_parser.add_argument('--library-id', type=int, help='Filter by library ID')
list_games_parser.add_argument('--completed', action='store_true', help='Show only completed games')
list_games_parser.add_argument('--platform', help='Filter by platform')
list_games_parser.add_argument('--genre', help='Filter by genre')

mark_game_parser = subparsers.add_parser('mark-game', help='Mark game as completed/uncompleted')
mark_game_parser.add_argument('id', type=int, help='Game ID')
mark_game_parser.add_argument('--completed', action='store_true', help='Mark as completed')
mark_game_parser.add_argument('--uncompleted', action='store_true', help='Mark as uncompleted')

play_game_parser = subparsers.add_parser('play-game', help='Record play session')
play_game_parser.add_argument('id', type=int, help='Game ID')
play_game_parser.add_argument('minutes', type=int, help='Minutes played')

stats_parser = subparsers.add_parser('stats', help='Show library statistics')
stats_parser.add_argument('library_id', type=int, help='Library ID')

delete_game_parser = subparsers.add_parser('delete-game', help='Delete a game')
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
    if not users:
        print("No users found.")
    for user in users:
        print(f"👤 {user.id}: {user.name}")

elif args.command == 'add-library':
    user = db.get(User, args.user_id)
    if not user:
        print(f"❌ User with ID {args.user_id} not found")
    else:
        lib = Library(title=args.title, user_id=args.user_id)
        db.add(lib)
        db.commit()
        print(f"📚 Added library: {lib.title} for user {user.name}")

elif args.command == 'list-libraries':
    query = db.query(Library)
    if args.user_id:
        query = query.filter(Library.user_id == args.user_id)
    libraries = query.all()

    if not libraries:
        print("No libraries found.")
    for lib in libraries:
        completion = lib.get_completion_stats()
        print(f"📘 {lib.id}: {lib.title} (User {lib.user_id}) - {completion:.1f}% completed")

elif args.command == 'add-game':
    lib = db.get(Library, args.library_id)
    if not lib:
        print(f"❌ Library with ID {args.library_id} not found")
    else:
        game = Game(
            title=args.title,
            genre=args.genre,
            platform=args.platform,
            library_id=args.library_id,
            rating=args.rating
        )
        db.add(game)
        db.commit()
        print(f"🎮 Added game: {game.title} | Genre: {game.genre} | Platform: {game.platform}")

elif args.command == 'list-games':
    query = db.query(Game)
    if args.library_id:
        query = query.filter(Game.library_id == args.library_id)
    if args.completed:
        query = query.filter(Game.completed == True)
    if args.platform:
        query = query.filter(Game.platform == args.platform)
    if args.genre:
        query = query.filter(Game.genre == args.genre)

    games = query.all()
    if not games:
        print("No games found.")
    for g in games:
        status = "✅" if g.completed else "❌"
        rating = "⭐" * g.rating if g.rating else "Not rated"
        play_time = f"{g.play_time} minutes" if g.play_time else "Not played"
        print(f"🎲 {g.id}: {g.title} - {g.genre} on {g.platform} {status}")
        print(f"   Rating: {rating} | Play time: {play_time}")

elif args.command == 'mark-game':
    game = db.get(Game, args.id)
    if not game:
        print(f"❌ Game with ID {args.id} not found")
    else:
        if args.completed:
            game.completed = True
            print(f"✅ Marked '{game.title}' as completed")
        elif args.uncompleted:
            game.completed = False
            print(f"❌ Marked '{game.title}' as not completed")
        db.commit()

elif args.command == 'play-game':
    game = db.get(Game, args.id)
    if not game:
        print(f"❌ Game with ID {args.id} not found")
    else:
        game.mark_as_played(args.minutes)
        db.commit()
        print(f"🎮 Recorded {args.minutes} minutes of play time for '{game.title}'")
        print(f"Total play time: {game.play_time} minutes")

elif args.command == 'stats':
    lib = db.get(Library, args.library_id)
    if not lib:
        print(f"❌ Library with ID {args.library_id} not found")
    else:
        completion = lib.get_completion_stats()
        total_play_time = sum(game.play_time for game in lib.games)
        print(f"📊 Statistics for library '{lib.title}':")
        print(f"Total games: {len(lib.games)}")
        print(f"Completion rate: {completion:.1f}%")
        print(f"Total play time: {total_play_time} minutes")
        if lib.games:
            avg_rating = sum(game.rating or 0 for game in lib.games) / len(lib.games)
            print(f"Average rating: {avg_rating:.1f}⭐")

elif args.command == 'delete-game':
    game = db.get(Game, args.id)
    if not game:
        print(f"❌ No game found with ID {args.id}")
    else:
        title = game.title
        db.delete(game)
        db.commit()
        print(f"🗑️ Deleted game: {title}")

else:
    parser.print_help()
