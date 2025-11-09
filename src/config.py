"""
Database configuration settings for PostgreSQL connection.
COMP-3005-A-F Assignment 3

I learned that it's good practice to separate configuration from code.
This file contains all the database connection parameters.

Student: Ahmad Bilal
Course: COMP-3005-A-F
"""

# Database connection parameters - configured for my local PostgreSQL setup
DB_CONFIG = {
    'host': 'localhost',        # PostgreSQL server host (running locally)
    'database': 'student_db',   # Database name I created for this assignment
    'user': 'ahmadbilal',       # My PostgreSQL username  
    'password': '',             # No password needed for local development
    'port': '5432'             # Default PostgreSQL port
}

# Connection timeout settings
CONNECTION_TIMEOUT = 30  # seconds
