# Game Library Manager

A simple CLI application to manage users and their game libraries. This application demonstrates a one-to-many relationship between users and libraries.

## Features

- Create and manage users
- Create and manage libraries for users
- List all users and their libraries
- Delete users (cascades to their libraries)
- Delete individual libraries

## Database Structure

- **User**: Represents a user who can own multiple libraries
  - Has a one-to-many relationship with Library
  - When a user is deleted, all their libraries are deleted too

- **Library**: Represents a game library owned by a user
  - Has a many-to-one relationship with User
  - Each library belongs to exactly one user

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install sqlalchemy
```

3. Initialize the database:
```bash
python -m lib.db.init_db
```

4. Run the application:
```bash
python -m lib.cli
```

## Usage

The application provides a simple menu-driven interface:

1. Create User - Create a new user with a unique username
2. List Users - Display all users and their libraries
3. Create Library - Create a new library for a specific user
4. List Libraries - Display all libraries or libraries for a specific user
5. Delete User - Delete a user and all their libraries
6. Delete Library - Delete a specific library
0. Exit - Exit the application

## Example

```bash
=== Game Library Manager ===
1. Create User
2. List Users
3. Create Library
4. List Libraries
5. Delete User
6. Delete Library
0. Exit

Enter your choice (0-6): 1
Enter username: john_doe

Enter your choice (0-6): 3
Enter user ID: 1
Enter library title: PC Games

Enter your choice (0-6): 2
Users:
- john_doe (ID: 1)
  Libraries:
    - PC Games
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
