# 🎮 Game Library Tracker

A command-line tool to manage your video game collection across multiple libraries.

## Features

- 👤 User Management
  - Create and list users
- 📚 Library Management
  - Create and manage game libraries for each user
  - View library statistics
- 🎲 Game Management
  - Add games with title, genre, platform, and rating
  - Mark games as completed/uncompleted
  - Track play time
  - Delete games
- 📊 Statistics
  - View completion rates
  - Track total play time
  - See average ratings

## Setup

1. Install dependencies:
```bash
pip install sqlalchemy alembic
```

2. Initialize the database:
```bash
alembic upgrade head
```

## Usage

### User Management
```bash
# Add a new user
python main.py add-user "John Doe"

# List all users
python main.py list-users
```

### Library Management
```bash
# Add a new library
python main.py add-library "PC Games" 1

# List all libraries
python main.py list-libraries

# List libraries for a specific user
python main.py list-libraries --user-id 1
```

### Game Management
```bash
# Add a new game
python main.py add-game "The Witcher 3" "RPG" "PC" 1 --rating 5

# List all games
python main.py list-games

# List games with filters
python main.py list-games --library-id 1 --completed --platform "PC" --genre "RPG"

# Mark a game as completed
python main.py mark-game 1 --completed

# Record play time
python main.py play-game 1 120  # Record 120 minutes of play time

# Delete a game
python main.py delete-game 1
```

### Statistics
```bash
# View library statistics
python main.py stats 1
```

## Database Schema

- Users
  - id (Primary Key)
  - name
  - created_at

- Libraries
  - id (Primary Key)
  - title
  - user_id (Foreign Key)
  - created_at

- Games
  - id (Primary Key)
  - title
  - genre
  - platform
  - completed
  - rating
  - play_time
  - last_played
  - library_id (Foreign Key)
