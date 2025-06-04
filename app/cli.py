from app.database import get_session
from app.models import User, Library

def list_users(session):
    """List all users"""
    users = session.query(User).all()
    if not users:
        print("\nNo users found")
        return

    print("\n=== Users ===")
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}")
        if user.libraries:
            print("  Libraries:")
            for lib in user.libraries:
                print(f"    - {lib.title} (ID: {lib.id})")
        else:
            print("  No libraries")

def list_libraries(session, user_id=None):
    """List all libraries or libraries for a specific user"""
    if user_id:
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            print("\nUser not found")
            return
        libraries = user.libraries
        print(f"\n=== Libraries for {user.username} ===")
    else:
        libraries = session.query(Library).all()
        print("\n=== All Libraries ===")

    if not libraries:
        print("No libraries found")
        return

    for lib in libraries:
        if user_id:
            print(f"ID: {lib.id}, Title: {lib.title}")
        else:
            print(f"ID: {lib.id}, Title: {lib.title}, Owner: {lib.user.username}")

def create_user(session):
    """Create a new user"""
    username = input("Enter username: ")

    # Check if username already exists
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print("Error: Username already exists")
        return

    user = User(username=username)
    session.add(user)
    try:
        session.commit()
        print(f"Created user: {username}")
    except:
        session.rollback()
        print("Error creating user")

def update_user(session):
    """Update a user's username"""
    list_users(session)
    user_id = input("\nEnter user ID to update: ")

    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print("Error: User not found")
        return

    new_username = input("Enter new username: ")
    if not new_username.strip():
        print("Error: Username cannot be empty")
        return

    # Check if new username already exists
    existing_user = session.query(User).filter_by(username=new_username).first()
    if existing_user and existing_user.id != user.id:
        print("Error: Username already exists")
        return

    user.username = new_username
    try:
        session.commit()
        print(f"Updated username to: {new_username}")
    except:
        session.rollback()
        print("Error updating user")

def delete_user(session):
    """Delete a user and all their libraries"""
    list_users(session)
    user_id = input("\nEnter user ID to delete: ")

    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print("Error: User not found")
        return

    confirm = input(f"Are you sure you want to delete user '{user.username}' and all their libraries? (y/n): ")
    if confirm.lower() != 'y':
        print("Operation cancelled")
        return

    try:
        session.delete(user)
        session.commit()
        print(f"Deleted user: {user.username}")
    except:
        session.rollback()
        print("Error deleting user")

def create_library(session):
    """Create a new library"""
    list_users(session)
    user_id = input("\nEnter user ID: ")
    title = input("Enter library title: ")

    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print("Error: User not found")
        return

    # Check if library title already exists for this user
    existing_library = session.query(Library).filter_by(user_id=user_id, title=title).first()
    if existing_library:
        print(f"Error: Library '{title}' already exists for this user")
        return

    library = Library(title=title, user_id=user.id)
    session.add(library)
    try:
        session.commit()
        print(f"Created library '{title}' for user '{user.username}'")
    except:
        session.rollback()
        print("Error creating library")

def update_library(session):
    """Update a library's title"""
    list_libraries(session)
    library_id = input("\nEnter library ID to update: ")

    library = session.query(Library).filter_by(id=library_id).first()
    if not library:
        print("Error: Library not found")
        return

    new_title = input("Enter new title: ")
    if not new_title.strip():
        print("Error: Title cannot be empty")
        return

    # Check if new title already exists for this user
    existing_library = session.query(Library).filter_by(user_id=library.user_id, title=new_title).first()
    if existing_library and existing_library.id != library.id:
        print(f"Error: Library '{new_title}' already exists for this user")
        return

    library.title = new_title
    try:
        session.commit()
        print(f"Updated library title to: {new_title}")
    except:
        session.rollback()
        print("Error updating library")

def delete_library(session):
    """Delete a library"""
    list_libraries(session)
    library_id = input("\nEnter library ID to delete: ")

    library = session.query(Library).filter_by(id=library_id).first()
    if not library:
        print("Error: Library not found")
        return

    confirm = input(f"Are you sure you want to delete library '{library.title}'? (y/n): ")
    if confirm.lower() != 'y':
        print("Operation cancelled")
        return

    try:
        session.delete(library)
        session.commit()
        print(f"Deleted library: {library.title}")
    except:
        session.rollback()
        print("Error deleting library")

def main_menu():
    """Display main menu"""
    print("\n=== Game Library Manager ===")
    print("1. List Users")
    print("2. List Libraries")
    print("3. Create User")
    print("4. Update User")
    print("5. Delete User")
    print("6. Create Library")
    print("7. Update Library")
    print("8. Delete Library")
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
            user_id = input("Enter user ID to filter libraries (or press Enter for all): ").strip()
            list_libraries(session, user_id if user_id else None)
        elif choice == "3":
            create_user(session)
        elif choice == "4":
            update_user(session)
        elif choice == "5":
            delete_user(session)
        elif choice == "6":
            create_library(session)
        elif choice == "7":
            update_library(session)
        elif choice == "8":
            delete_library(session)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
