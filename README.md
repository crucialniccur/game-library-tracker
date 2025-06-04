# Game Library Manager CLI

A command-line interface application for managing users and their game libraries. Built with Python and SQLAlchemy.

## Features

- User Management (Create, Read, Update, Delete)
- Library Management (Create, Read, Update, Delete)
- One-to-Many relationship between Users and Libraries
- Data persistence using SQLite database

## Prerequisites

- Python 3.8 or higher
- pipenv

## Installation & Setup

```bash
# Clone the repository
git clone [<repository-url>](https://github.com/crucialniccur/game-library-tracker)
cd game-library-tracker

# Install dependencies and activate virtual environment
pipenv install
pipenv shell

# Initialize the database with sample data
python3 seed.py
```

## Usage

1. Start the CLI application:
```bash
python3 -m app.cli
```

2. Available Commands:
```
1. List Users
2. List Libraries
3. Create User
4. Update User
5. Delete User
6. Create Library
7. Update Library
8. Delete Library
0. Exit
```

### Example Workflow

1. Create a new user:
```
Choose option: 3
Enter username: Alex
```

2. Create libraries for the user:
```
Choose option: 6
# You'll see list of users with their IDs
Enter user ID: (enter Alex's ID)
Enter library title: PS5 Games
```

3. View all libraries:
```
Choose option: 2
# Press Enter when asked for user ID to see all libraries
```

4. View libraries for specific user:
```
Choose option: 2
Enter user ID: (enter user's ID)
```

## Database Schema

### Users Table
- id (Primary Key)
- username (Unique, Non-nullable)

### Libraries Table
- id (Primary Key)
- title (Non-nullable)
- user_id (Foreign Key to users.id)

### Relationships
- One-to-Many relationship between User and Library
- One user can have multiple libraries
- Each library belongs to exactly one user
- When a user is deleted, all their libraries are automatically deleted (cascade delete)

## Error Handling

The application includes error handling for:
- Duplicate usernames
- Invalid user IDs
- Invalid library IDs
- Empty input validation
- Confirmation for delete operations

## Troubleshooting

If you encounter any issues:
1. Exit the application (Option 0)
2. Delete the database file: `rm game_library.db`
3. Run `python3 seed.py` to start fresh
4. Start the application again: `python3 -m app.cli`

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
