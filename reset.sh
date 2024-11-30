#!/bin/bash

# Navigate to the directory where your Flask application is located
# Update the path below to the directory containing your Flask app
cd /Users/cooperkeenan/Library/CloudStorage/OneDrive-EdinburghNapierUniversity/Third_Year/Web-Tech/FlatFinder

# Activate your virtual environment if needed
# Replace "venv" with the name of your virtual environment folder if it's different
source venv/bin/activate

# Drop the database
flask drop_db

# Initialize the database
flask init_db

# Run the models.py to set up your models
python3 models.py

# Run the import_data.py to populate your database
python3 import_data.py

# Deactivate the virtual environment
deactivate
