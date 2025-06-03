#!/usr/bin/env python3

import sys
import os
from typing import Optional, Union

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.models import User, Library
from db.database import get_db

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
        if user.libraries:
            print("  Libraries:")
            for library in user.libraries:
                print(f"    - {library.title}")
        else:
            print("  No libraries")

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

def list_libraries(session: Session, user_id: Optional[int] = None):
    """List all libraries or libraries for a specific user"""
    if user_id is not None:
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
        print(f"- {lib.title} (ID: {lib.id}, Owner: {lib.user.username})")

def delete_user(session: Session, user_id: int):
    """Delete a user and all their libraries"""
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        print(f"Error: User with ID {user_id} not found!")
        return

    username = user.username
    session.delete(user)
    session.commit()
    print(f"User '{username}' and all their libraries have been deleted!")

def delete_library(session: Session, library_id: int):
    """Delete a library"""
    library = session.query(Library).filter(Library.id == library_id).first()
    if not library:
        print(f"Error: Library with ID {library_id} not found!")
        return

    title = library.title
    session.delete(library)
    session.commit()
    print(f"Library '{title}' has been deleted!")

def main():
    """Main CLI interface"""
    session = next(get_db())

    while True:
        print("\n=== Game Library Manager ===")
        print("1. Create User")
        print("2. List Users")
        print("3. Create Library")
        print("4. List Libraries")
        print("5. Delete User")
        print("6. Delete Library")
        print("0. Exit")

        choice = input("\nEnter your choice (0-6): ")

        if choice == "1":
            username = input("Enter username: ")
            create_user(session, username)

        elif choice == "2":
            list_users(session)

        elif choice == "3":
            user_id = input("Enter user ID: ")
            title = input("Enter library title: ")
            try:
                create_library(session, int(user_id), title)
            except ValueError:
                print("Error: User ID must be a number!")

        elif choice == "4":
            user_id = input("Enter user ID (press Enter to list all): ")
            try:
                list_libraries(session, int(user_id) if user_id else None)
            except ValueError:
                if user_id:  # Only show error if user actually entered something
                    print("Error: User ID must be a number!")
                else:
                    list_libraries(session)

        elif choice == "5":
            user_id = input("Enter user ID to delete: ")
            try:
                delete_user(session, int(user_id))
            except ValueError:
                print("Error: User ID must be a number!")

        elif choice == "6":
            library_id = input("Enter library ID to delete: ")
            try:
                delete_library(session, int(library_id))
            except ValueError:
                print("Error: Library ID must be a number!")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
