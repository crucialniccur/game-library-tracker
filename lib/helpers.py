from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import User, Library, Game

# Create database engine and session
engine = create_engine('sqlite:///game_library.db')
Session = sessionmaker(bind=engine)

def list_all_users():
    """List all users in the database"""
    session = Session()
    users = session.query(User).all()
    if users:
        print("\nUsers:")
        for user in users:
            print(f"- {user.username}")
    else:
        print("No users found.")
    session.close()

def add_new_user(username):
    """Add a new user to the database"""
    session = Session()
    try:
        user = User(username=username)
        session.add(user)
        session.commit()
        print(f"User '{username}' added successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")
        session.rollback()
    finally:
        session.close()

def create_new_library(name, username):
    """Create a new library for a user"""
    session = Session()
    try:
        user = session.query(User).filter_by(username=username).first()
        if user:
            library = Library(name=name, user=user)
            session.add(library)
            session.commit()
            print(f"Library '{name}' created for user '{username}'!")
        else:
            print(f"User '{username}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")
        session.rollback()
    finally:
        session.close()

def list_all_libraries():
    """List all libraries and their owners"""
    session = Session()
    libraries = session.query(Library).all()
    if libraries:
        print("\nLibraries:")
        for library in libraries:
            print(f"- {library.name} (Owner: {library.user.username})")
    else:
        print("No libraries found.")
    session.close()

def add_game_to_library(title, library_name, completion, playtime, rating):
    """Add a game to a library"""
    session = Session()
    try:
        library = session.query(Library).filter_by(name=library_name).first()
        if library:
            game = Game(
                title=title,
                library=library,
                completion_rate=float(completion),
                playtime_hours=float(playtime),
                rating=int(rating)
            )
            session.add(game)
            session.commit()
            print(f"Game '{title}' added to library '{library_name}'!")
        else:
            print(f"Library '{library_name}' not found.")
    except ValueError:
        print("Error: Please enter valid numbers for completion, playtime, and rating.")
    except Exception as e:
        print(f"Error: {str(e)}")
        session.rollback()
    finally:
        session.close()

def list_games_in_library(library_name):
    """List all games in a library"""
    session = Session()
    library = session.query(Library).filter_by(name=library_name).first()
    if library:
        if library.games:
            print(f"\nGames in {library_name}:")
            for game in library.games:
                print(f"- {game.title}")
                print(f"  Completion: {game.completion_rate}%")
                print(f"  Playtime: {game.playtime_hours} hours")
                print(f"  Rating: {game.rating}/10")
        else:
            print(f"No games found in library '{library_name}'.")
    else:
        print(f"Library '{library_name}' not found.")
    session.close()

def delete_game_from_library(title, library_name):
    """Delete a game from a library"""
    session = Session()
    try:
        library = session.query(Library).filter_by(name=library_name).first()
        if library:
            game = session.query(Game).filter_by(title=title, library_id=library.id).first()
            if game:
                session.delete(game)
                session.commit()
                print(f"Game '{title}' deleted from library '{library_name}'!")
            else:
                print(f"Game '{title}' not found in library '{library_name}'.")
        else:
            print(f"Library '{library_name}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")
        session.rollback()
    finally:
        session.close()

def view_library_stats(library_name):
    """View statistics for a library"""
    session = Session()
    library = session.query(Library).filter_by(name=library_name).first()
    if library:
        games = library.games
        if games:
            total_games = len(games)
            avg_completion = sum(game.completion_rate for game in games) / total_games
            total_playtime = sum(game.playtime_hours for game in games)
            avg_rating = sum(game.rating for game in games) / total_games

            print(f"\nStatistics for {library_name}:")
            print(f"Total Games: {total_games}")
            print(f"Average Completion Rate: {avg_completion:.1f}%")
            print(f"Total Playtime: {total_playtime:.1f} hours")
            print(f"Average Rating: {avg_rating:.1f}/10")
        else:
            print(f"No games found in library '{library_name}'.")
    else:
        print(f"Library '{library_name}' not found.")
    session.close()
