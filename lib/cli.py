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
    print("\n=== Game Library Tracker CLI ===")
    print("1. List Users")
    print("2. Add User")
    print("3. Create Library")
    print("4. List Libraries")
    print("5. Add Game")
    print("6. List Games")
    print("7. Delete Game")
    print("8. View Statistics")
    print("9. Exit")
    print("\nEnter your choice (1-9): ")

def get_input(prompt, allow_empty=False):
    """Get user input with optional empty check"""
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("Error: Input cannot be empty. Please try again.")

def main():
    while True:
        display_menu()
        choice = get_input("", allow_empty=True)

        if choice == "1":
            list_all_users()
        elif choice == "2":
            username = get_input("Enter username: ")
            add_new_user(username)
        elif choice == "3":
            name = get_input("Enter library name: ")
            username = get_input("Enter username: ")
            create_new_library(name, username)
        elif choice == "4":
            list_all_libraries()
        elif choice == "5":
            title = get_input("Enter game title: ")
            library = get_input("Enter library name: ")
            completion = get_input("Enter completion percentage (0-100): ")
            playtime = get_input("Enter playtime in hours: ")
            rating = get_input("Enter rating (1-10): ")
            add_game_to_library(title, library, completion, playtime, rating)
        elif choice == "6":
            library = get_input("Enter library name: ")
            list_games_in_library(library)
        elif choice == "7":
            title = get_input("Enter game title: ")
            library = get_input("Enter library name: ")
            delete_game_from_library(title, library)
        elif choice == "8":
            library = get_input("Enter library name: ")
            view_library_stats(library)
        elif choice == "9":
            print("Thank you for using Game Library Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
