# Game Library Manager

A simple CLI application to manage game libraries. Users can create libraries and add games to them.

## Features

- Create users
- Create game libraries for users
- Add games to libraries
- View all data in a hierarchical structure

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Seed the database with sample data:
```bash
python seed.py
```

4. Run the application:
```bash
python -m app.cli
```

## Usage Example

```
=== Game Library Manager ===
1. Create User
2. Create Library
3. Add Game
4. View All
0. Exit

Choose an option: 4

User: john_doe
  Library: PC Games
    Game: The Witcher 3
    Game: Cyberpunk 2077
  Library: Console Games
    Game: God of War

User: alice_smith
  Library: Mobile Games
    Game: Pokemon GO
```

## Project Structure

```
game-library-tracker/
├── lib/                    # Main package directory
│   ├── __init__.py
│   ├── cli.py             # CLI interface
│   └── db/                # Database related code
│       ├── __init__.py
│       ├── database.py    # Database connection
│       ├── init_db.py     # Database initialization
│       └── models.py      # SQLAlchemy models
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── Pipfile               # Pipenv dependencies
├── seed.py               # Database seeder
└── alembic.ini           # Alembic migrations config
```

## Usage

The application provides a simple menu-driven interface:

1. Create User - Create a new user with a unique username
2. Create Library - Create a new library for a specific user
3. Add Game - Add a game to a specific library
4. View All - View all users and their libraries
0. Exit - Exit the application

## Example

```bash
=== Game Library Manager ===
1. Create User
2. Create Library
3. Add Game
4. View All
0. Exit

Enter your choice (0-4): 4
Users:
- john_gamer (ID: 1)
  Libraries:
    - PC Games
    - PlayStation Games
- alice_player (ID: 2)
  Libraries:
    - Nintendo Switch
    - Mobile Games
- bob_games (ID: 3)
  Libraries:
    - Xbox Collection
```

## Database Schema

### Users
- id (Primary Key)
- username (String, Unique)

### Libraries
- id (Primary Key)
- title (String)
- user_id (Foreign Key to Users)

## Error Handling

The application includes error handling for:
- Duplicate usernames
- Invalid user IDs
- Invalid library IDs
- Database connection issues

All errors are displayed with clear, user-friendly messages.
