#!/usr/bin/env python3

from helpers import (
    list_all_users,
    add_new_user,
    create_new_library,
    list_all_libraries,
    add_game_to_library,
    list_games_in_library,
    delete_game_from_library,
    view_library_stats
)

def display_menu():
    """Display the main menu options"""
    print("\n=== Game Library Tracker ===")
    print("1. List all users")
    print("2. Add new user")
    print("3. Create new library")
    print("4. List all libraries")
    print("5. Add game to library")
    print("6. List games in library")
    print("7. Delete game")
    print("8. View library statistics")
    print("0. Exit")
    print("\nEnter your choice: ")

def get_user_input(prompt):
    """Get user input with validation"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")

def main():
    while True:
        display_menu()
        choice = input().strip()

        if choice == "1":
            list_all_users()

        elif choice == "2":
            username = get_user_input("Enter username: ")
            add_new_user(username)

        elif choice == "3":
            name = get_user_input("Enter library name: ")
            username = get_user_input("Enter username: ")
            create_new_library(name, username)

        elif choice == "4":
            list_all_libraries()

        elif choice == "5":
            title = get_user_input("Enter game title: ")
            library = get_user_input("Enter library name: ")
            completion = input("Enter completion percentage (0-100): ")
            playtime = input("Enter playtime in hours: ")
            rating = input("Enter rating (1-5): ")
            add_game_to_library(title, library, completion, playtime, rating)

        elif choice == "6":
            library = get_user_input("Enter library name: ")
            list_games_in_library(library)

        elif choice == "7":
            title = get_user_input("Enter game title: ")
            library = get_user_input("Enter library name: ")
            delete_game_from_library(title, library)

        elif choice == "8":
            library = get_user_input("Enter library name: ")
            view_library_stats(library)

        elif choice == "0":
            print("Thank you for using Game Library Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
