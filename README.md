# Game Library Tracker

A command-line interface (CLI) application to manage your video game collection across multiple libraries.

## Features

- User Management
  - Create and manage users
  - List all users in the system
- Library Management
  - Create and manage game libraries for each user
  - View library statistics and details
- Game Management
  - Add games with validated information (title, genre, platform, rating)
  - Track game completion status
  - Record and update play time
  - Remove games from libraries
- Statistics
  - View completion rates for libraries
  - Track total play time
  - Calculate average ratings

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd game-library-tracker
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
.\venv\Scripts\activate  # On Windows
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
alembic upgrade head
```

## Usage

### User Management
```bash
# Add a new user (username must be 3-50 characters)
python main.py add-user "John Doe"

# List all users
python main.py list-users
```

### Library Management
```bash
# Add a new library (requires valid user_id)
python main.py add-library "PC Games" 1

# List all libraries
python main.py list-libraries

# List libraries for a specific user
python main.py list-libraries --user-id 1
```

### Game Management
```bash
# Add a new game (rating must be between 1-5)
python main.py add-game "The Witcher 3" "RPG" "PC" 1 --rating 5

# List games (supports various filters)
python main.py list-games
python main.py list-games --library-id 1
python main.py list-games --completed
python main.py list-games --platform "PC"
python main.py list-games --genre "RPG"

# Update game completion status
python main.py mark-game 1 --completed

# Record play time (in minutes)
python main.py play-game 1 120

# Delete a game
python main.py delete-game 1
```

### Statistics
```bash
# View library statistics (requires library_id)
python main.py stats 1
```

## Input Validation

The application includes validation for:
- Usernames (3-50 characters)
- Library names (1-100 characters)
- Game titles (1-100 characters)
- Completion status (boolean)
- Play time (positive integer)
- Ratings (1-5)

## Database Schema

### Users
- id (Primary Key)
- name (String)
- created_at (DateTime)

### Libraries
- id (Primary Key)
- title (String)
- user_id (Foreign Key)
- created_at (DateTime)

### Games
- id (Primary Key)
- title (String)
- genre (String)
- platform (String)
- completed (Boolean)
- rating (Integer)
- play_time (Integer)
- last_played (DateTime)
- library_id (Foreign Key)

## Error Handling

The application includes comprehensive error handling for:
- Invalid input validation
- Database constraints
- Non-existent resources
- Invalid operations

All errors are displayed with clear, user-friendly messages to help troubleshoot issues.
