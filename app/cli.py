from app.database import get_session
from app.models import User, Library, Game

def list_users(session):
    """List all users"""
    users = session.query(User).all()
    if not users:
        print("\nNo users found")
        return

    print("\n=== Users ===")
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}")

def list_libraries(session):
    """List all libraries"""
    libraries = session.query(Library).all()
    if not libraries:
        print("\nNo libraries found")
        return

    print("\n=== Libraries ===")
    for lib in libraries:
        print(f"ID: {lib.id}, Title: {lib.title}, Owner: {lib.user.username}")

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
    list_users(session)
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
    list_libraries(session)
    library_id = input("\nEnter library ID: ")
    title = input("Enter game title: ")
    genre = input("Enter game genre: ")
    platform = input("Enter game platform: ")

    library = session.query(Library).filter_by(id=library_id).first()
    if library:
        game = Game(
            title=title,
            genre=genre,
            platform=platform,
            library_id=library.id
        )
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
                        print(f"    Game: {game.title} ({game.genre}, {game.platform})")
                else:
                    print("    No games")
        else:
            print("  No libraries")

def main_menu():
    """Display main menu"""
    print("\n=== Game Library Manager ===")
    print("1. List Users")
    print("2. List Libraries")
    print("3. Create User")
    print("4. Create Library")
    print("5. Add Game")
    print("6. View All")
    print("0. Exit")
    return input("Choose an option: ")

def main():
    """Main application loop"""
    session = get_session()

    while True:
        choice = main_menu()

        if choice == "1":
            list_users(session)
        elif choice == "2":
            list_libraries(session)
        elif choice == "3":
            create_user(session)
        elif choice == "4":
            create_library(session)
        elif choice == "5":
            add_game(session)
        elif choice == "6":
            view_all(session)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
