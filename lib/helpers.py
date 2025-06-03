from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import User, Library, Game

# Create database engine and session
engine = create_engine('sqlite:///game_library.db')
Session = sessionmaker(bind=engine)

def validate_username(username):
    """Validate username input"""
    if not username or not username.strip():
        return False, "Username cannot be empty"
    if len(username) < 3:
        return False, "Username must be at least 3 characters long"
    if len(username) > 50:
        return False, "Username must be less than 50 characters"
    if not username.replace("_", "").isalnum():
        return False, "Username can only contain letters, numbers, and underscores"
    return True, None

def validate_library_name(name):
    """Validate library name input"""
    if not name or not name.strip():
        return False, "Library name cannot be empty"
    if len(name) < 2:
        return False, "Library name must be at least 2 characters long"
    if len(name) > 50:
        return False, "Library name must be less than 50 characters"
    return True, None

def validate_game_title(title):
    """Validate game title input"""
    if not title or not title.strip():
        return False, "Game title cannot be empty"
    if len(title) < 1:
        return False, "Game title must be at least 1 character long"
    if len(title) > 100:
        return False, "Game title must be less than 100 characters"
    return True, None

def validate_completion_rate(rate):
    """Validate completion rate input"""
    try:
        rate_float = float(rate)
        if rate_float < 0 or rate_float > 100:
            return False, "Completion rate must be between 0 and 100"
        return True, None
    except ValueError:
        return False, "Completion rate must be a number"

def validate_playtime(time):
    """Validate playtime input"""
    try:
        time_float = float(time)
        if time_float < 0:
            return False, "Playtime cannot be negative"
        if time_float > 10000:
            return False, "Playtime seems too high (max 10000 hours)"
        return True, None
    except ValueError:
        return False, "Playtime must be a number"

def validate_rating(rating):
    """Validate rating input"""
    try:
        rating_int = int(rating)
        if rating_int < 1 or rating_int > 10:
            return False, "Rating must be between 1 and 10"
        return True, None
    except ValueError:
        return False, "Rating must be a whole number"

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
    # Validate username
    is_valid, error = validate_username(username)
    if not is_valid:
        print(f"Error: {error}")
        return False

    session = Session()
    try:
        # Check if username already exists
        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            print(f"Error: Username '{username}' already exists")
            return False

        user = User(username=username)
        session.add(user)
        session.commit()
        print(f"User '{username}' added successfully!")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        session.rollback()
        return False
    finally:
        session.close()

def create_new_library(name, username):
    """Create a new library for a user"""
    # Validate library name
    is_valid, error = validate_library_name(name)
    if not is_valid:
        print(f"Error: {error}")
        return False

    session = Session()
    try:
        # Check if library name already exists for the user
        user = session.query(User).filter_by(username=username).first()
        if not user:
            print(f"Error: User '{username}' not found")
            return False

        existing_library = session.query(Library).filter_by(name=name, user_id=user.id).first()
        if existing_library:
            print(f"Error: Library '{name}' already exists for user '{username}'")
            return False

        library = Library(name=name, user=user)
        session.add(library)
        session.commit()
        print(f"Library '{name}' created for user '{username}'!")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        session.rollback()
        return False
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
    # Validate all inputs
    validations = [
        validate_game_title(title),
        validate_completion_rate(completion),
        validate_playtime(playtime),
        validate_rating(rating)
    ]

    for is_valid, error in validations:
        if not is_valid:
            print(f"Error: {error}")
            return False

    session = Session()
    try:
        library = session.query(Library).filter_by(name=library_name).first()
        if not library:
            print(f"Error: Library '{library_name}' not found")
            return False

        # Check if game already exists in the library
        existing_game = session.query(Game).filter_by(title=title, library_id=library.id).first()
        if existing_game:
            print(f"Error: Game '{title}' already exists in library '{library_name}'")
            return False

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
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        session.rollback()
        return False
    finally:
        session.close()

def list_games_in_library(library_name, completed=None, platform=None, genre=None):
    """List games in a library with optional filters"""
    session = Session()
    try:
        library = session.query(Library).filter_by(name=library_name).first()
        if not library:
            print(f"Error: Library '{library_name}' not found")
            return False

        # Build query with filters
        query = session.query(Game).filter_by(library_id=library.id)

        if completed is not None:
            query = query.filter(Game.completed == completed)
        if platform:
            query = query.filter(Game.platform == platform)
        if genre:
            query = query.filter(Game.genre == genre)

        games = query.all()

        if games:
            print(f"\nGames in library '{library_name}':")
            for game in games:
                completion_status = "✓" if game.completed else "✗"
                print(f"- {game.title} [{game.platform}] ({game.genre}) "
                      f"Rating: {game.rating}/5 | "
                      f"Playtime: {game.playtime_hours}h | "
                      f"Completed: {completion_status}")
        else:
            print(f"No games found in library '{library_name}' with the specified filters.")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
    finally:
        session.close()

def delete_game_from_library(title, library_name):
    """Delete a game from a library"""
    if not title or not title.strip():
        print("Error: Game title cannot be empty")
        return False

    session = Session()
    try:
        library = session.query(Library).filter_by(name=library_name).first()
        if not library:
            print(f"Error: Library '{library_name}' not found")
            return False

        game = session.query(Game).filter_by(title=title, library_id=library.id).first()
        if not game:
            print(f"Error: Game '{title}' not found in library '{library_name}'")
            return False

        session.delete(game)
        session.commit()
        print(f"Game '{title}' deleted from library '{library_name}'!")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        session.rollback()
        return False
    finally:
        session.close()

def view_library_stats(library_name):
    """View statistics for a library"""
    session = Session()
    library = session.query(Library).filter_by(name=library_name).first()
    if not library:
        print(f"Error: Library '{library_name}' not found")
        return False

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
    session.close()
    return True
