from .database import get_session
from .models import User, Library, Game

def create_user(session):
    """Create a new user"""
    username = input("Enter username: ")
    user = User(username=username)
    session.add(user)
    try:
        session.commit()
        print(f"Created user: {username}")
    except:
        session.rollback()
        print("Error: Username already exists")

def create_library(session):
    """Create a new library"""
    print("\nAvailable users:")
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}")

    user_id = input("\nEnter user ID: ")
    title = input("Enter library title: ")

    user = session.query(User).filter_by(id=user_id).first()
    if user:
        library = Library(title=title, user_id=user.id)
        session.add(library)
        session.commit()
        print(f"Created library '{title}' for user '{user.username}'")
    else:
        print("Error: User not found")

def add_game(session):
    """Add a game to a library"""
    print("\nAvailable libraries:")
    libraries = session.query(Library).all()
    for lib in libraries:
        print(f"ID: {lib.id}, Title: {lib.title}, Owner: {lib.user.username}")

    library_id = input("\nEnter library ID: ")
    title = input("Enter game title: ")

    library = session.query(Library).filter_by(id=library_id).first()
    if library:
        game = Game(title=title, library_id=library.id)
        session.add(game)
        session.commit()
        print(f"Added game '{title}' to library '{library.title}'")
    else:
        print("Error: Library not found")

def view_all(session):
    """View all users and their libraries/games"""
    users = session.query(User).all()
    if not users:
        print("No users found")
        return

    for user in users:
        print(f"\nUser: {user.username}")
        if user.libraries:
            for library in user.libraries:
                print(f"  Library: {library.title}")
                if library.games:
                    for game in library.games:
                        print(f"    Game: {game.title}")
                else:
                    print("    No games")
        else:
            print("  No libraries")

def main_menu():
    """Display main menu"""
    print("\n=== Game Library Manager ===")
    print("1. Create User")
    print("2. Create Library")
    print("3. Add Game")
    print("4. View All")
    print("0. Exit")
    return input("Choose an option: ")

def main():
    """Main application loop"""
    session = get_session()

    while True:
        choice = main_menu()

        if choice == "1":
            create_user(session)
        elif choice == "2":
            create_library(session)
        elif choice == "3":
            add_game(session)
        elif choice == "4":
            view_all(session)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
