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

The application provides a command-line interface with various commands. Here are the available commands:

### User Management
```bash
# List all users
game-tracker users

# Add a new user
game-tracker add-user "John Doe"
```

### Library Management
```bash
# Create a new library for a user
game-tracker create-library "PC Games" "John Doe"

# List all libraries
game-tracker libraries
```

### Game Management
```bash
# Add a new game with optional parameters
game-tracker add-game "The Witcher 3" "PC Games" --completion 75 --playtime 120.5 --rating 5

# List games with various filters
game-tracker list-games "PC Games"
game-tracker list-games "PC Games" --completed
game-tracker list-games "PC Games" --platform "PC" --genre "RPG"

# Delete a game
game-tracker delete-game "The Witcher 3" "PC Games"
```

### Statistics
```bash
# View library statistics
game-tracker stats "PC Games"
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
