#!/usr/bin/env python3

import sys
import os
from typing import Optional

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
try:
    # Try relative import first (when running as a module)
    from .db.models import User, Library, Game
    from .db.database import get_db
except ImportError:
    # Fall back to absolute import (when running as a script)
    from lib.db.models import User, Library, Game
    from lib.db.database import get_db

def create_user(session: Session, username: str) -> Optional[User]:
    """Create a new user"""
    user = User(username=username)
    session.add(user)
    try:
        session.commit()
        print(f"User '{username}' created successfully!")
        return user
    except IntegrityError:
        session.rollback()
        print(f"Error: Username '{username}' already exists!")
        return None

def list_users(session: Session):
    """List all users"""
    users = session.query(User).all()
    if not users:
        print("No users found!")
        return

    print("\nUsers:")
    for user in users:
        print(f"- {user.username} (ID: {user.id})")

def list_libraries(session: Session, user_id: Optional[int] = None):
    """List all libraries or libraries for a specific user"""
    if user_id:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            print(f"Error: User with ID {user_id} not found!")
            return
        libraries = user.libraries
        print(f"\nLibraries for user '{user.username}':")
    else:
        libraries = session.query(Library).all()
        print("\nAll Libraries:")

    if not libraries:
        print("No libraries found!")
        return

    for lib in libraries:
        if user_id:
            print(f"- {lib.title} (ID: {lib.id})")
        else:
            print(f"- {lib.title} (ID: {lib.id}, Owner: {lib.user.username})")

def list_games(session: Session, library_id: Optional[int] = None):
    """List all games or games in a specific library"""
    if library_id:
        library = session.query(Library).filter(Library.id == library_id).first()
        if not library:
            print(f"Error: Library with ID {library_id} not found!")
            return
        games = library.games
        print(f"\nGames in library '{library.title}':")
    else:
        games = session.query(Game).all()
        print("\nAll Games:")

    if not games:
        print("No games found!")
        return

    for game in games:
        if library_id:
            print(f"- {game.title} (ID: {game.id})")
        else:
            print(f"- {game.title} (ID: {game.id}, Library: {game.library.title})")

def list_everything(session: Session):
    """List all users, their libraries and games"""
    users = session.query(User).all()
    if not users:
        print("No users found!")
        return

    print("\nUsers and their Libraries/Games:")
    for user in users:
        print(f"\n- {user.username} (ID: {user.id})")
        if user.libraries:
            for library in user.libraries:
                print(f"  └── {library.title} (ID: {library.id})")
                if library.games:
                    for game in library.games:
                        print(f"      └── {game.title} (ID: {game.id})")
                else:
                    print("      (No games)")
        else:
            print("  (No libraries)")

def create_library(session: Session, user_id: int, title: str) -> Optional[Library]:
    """Create a new library for a user"""
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        print(f"Error: User with ID {user_id} not found!")
        return None

    library = Library(title=title, user_id=user_id)
    session.add(library)
    session.commit()
    print(f"Library '{title}' created for user '{user.username}'!")
    return library

def add_game(session: Session, library_id: int, title: str) -> Optional[Game]:
    """Add a new game to a library"""
    library = session.query(Library).filter(Library.id == library_id).first()
    if not library:
        print(f"Error: Library with ID {library_id} not found!")
        return None

    game = Game(title=title, library_id=library_id)
    session.add(game)
    session.commit()
    print(f"Game '{title}' added to library '{library.title}'!")
    return game

def delete_game(session: Session, game_id: int):
    """Delete a game"""
    game = session.query(Game).filter(Game.id == game_id).first()
    if not game:
        print(f"Error: Game with ID {game_id} not found!")
        return

    title = game.title
    library_title = game.library.title
    session.delete(game)
    session.commit()
    print(f"Game '{title}' has been deleted from library '{library_title}'!")

def main():
    """Main CLI interface"""
    session = next(get_db())

    while True:
        print("\n=== Game Library Manager ===")
        print("1. Create User")
        print("2. Create Library")
        print("3. Add Game")
        print("4. Delete Game")
        print("5. List Users")
        print("6. List Libraries")
        print("7. List Games")
        print("8. List Everything")
        print("0. Exit")

        choice = input("\nEnter your choice (0-8): ")

        if choice == "1":
            username = input("Enter username: ")
            create_user(session, username)

        elif choice == "2":
            user_id = input("Enter user ID: ")
            title = input("Enter library title: ")
            try:
                create_library(session, int(user_id), title)
            except ValueError:
                print("Error: User ID must be a number!")

        elif choice == "3":
            library_id = input("Enter library ID: ")
            title = input("Enter game title: ")
            try:
                add_game(session, int(library_id), title)
            except ValueError:
                print("Error: Library ID must be a number!")

        elif choice == "4":
            game_id = input("Enter game ID: ")
            try:
                delete_game(session, int(game_id))
            except ValueError:
                print("Error: Game ID must be a number!")

        elif choice == "5":
            list_users(session)

        elif choice == "6":
            user_id = input("Enter user ID (press Enter to list all): ").strip()
            try:
                list_libraries(session, int(user_id) if user_id else None)
            except ValueError:
                print("Error: User ID must be a number!")

        elif choice == "7":
            library_id = input("Enter library ID (press Enter to list all): ").strip()
            try:
                list_games(session, int(library_id) if library_id else None)
            except ValueError:
                print("Error: Library ID must be a number!")

        elif choice == "8":
            list_everything(session)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
