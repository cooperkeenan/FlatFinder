#!/bin/bash

# Navigate to the directory where your Flask application is located
cd /Users/cooperkeenan/Library/CloudStorage/OneDrive-EdinburghNapierUniversity/Third_Year/Web-Tech/FlatFinder

# Activate your virtual environment
# Replace "flenv" with the correct virtual environment folder name
source flenv/bin/activate

# Drop the database
flask drop_db

# Initialize the database
flask init_db

# Initialize Flask-Migrate if not already initialized
# If migrations folder exists, skip this step
if [ ! -d "migrations" ]; then
    flask db init
fi

# Create a new migration
flask db migrate -m "Add password_hash to User model and integrate Flask-Bcrypt"

# Apply the migration
flask db upgrade

# Run the import_data.py to populate your database
python3 import_data.py

# Deactivate the virtual environment
deactivate
