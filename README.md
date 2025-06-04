# Game Library Manager

A CLI application to manage your game libraries. Users can create libraries and add games to them with detailed information like genre, platform, and play status.

## Features

- Create users with unique usernames
- Create game libraries for users
- Add games with detailed information (title, genre, platform, completion status)
- View all data in a hierarchical structure

## Prerequisites

- Python 3.8 or higher
- Pipenv

## Setup Instructions

1. Clone and navigate to the project:
```bash
git clone [<repository-url>](https://github.com/crucialniccur/game-library-tracker)
cd game-library-tracker
```

2. Install dependencies using Pipenv:
```bash
pipenv install
pipenv shell
```

3. Initialize the database:
```bash
alembic upgrade head
```

4. (Optional) Seed the database with sample data:
```bash
python seed.py
```

5. Run the application:
```bash
python -m app.cli
```

## Usage

The application provides a simple menu-driven interface:

1. **Create User** - Create a new user with a unique username
2. **Create Library** - Create a new library for a specific user
3. **Add Game** - Add a game to a specific library with the following details:
   - Title

4. **View All** - View all users and their libraries
0. **Exit** - Exit the application

## Example Output

```
=== Game Library Manager ===
Users:
- john_doe
  Libraries:
    - PC Games
      - The Witcher 3 (RPG, PC)
      - Cyberpunk 2077 (RPG, PC)
    - Console Games
      - God of War (Action-Adventure, PlayStation)
- alice_smith
  Libraries:
    - Mobile Games
      - Pokemon GO (AR, Mobile)
```

## Database Schema

### Users
- id (Primary Key)
- username (String, Unique)

### Libraries
- id (Primary Key)
- title (String)
- user_id (Foreign Key to Users)

### Games
- id (Primary Key)
- title (String)
- genre (String)
- platform (String)
- completed (Boolean, Optional)
- play_time (Integer, Optional)
- rating (Integer, Optional)
- library_id (Foreign Key to Libraries)

## Error Handling

The application includes error handling for:
- Duplicate usernames
- Invalid user IDs
- Invalid library IDs
- Missing required game information
- Database connection issues

All errors are displayed with clear, user-friendly messages.
