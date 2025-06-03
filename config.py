# This file contains the database settings

# Import the os module to work with file paths
import os

# Get the folder where this file is located
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Name of our database file
DB_FILE = "game_library.db"

# Full path to our database file (will be created in the same folder as this file)
DB_PATH = os.path.join(CURRENT_FOLDER, DB_FILE)

# The database URL that SQLAlchemy will use
# sqlite:/// means we're using SQLite database
# We just add our database path after sqlite:///
DATABASE_URL = f"sqlite:///{DB_PATH}"
