# Student Management System - Database Application

**COMP-3005-A-F Assignment 3: Database Interaction with PostgreSQL**

**Student:** Ahmad Bilal    
**Course:** COMP-3005-A-F  
**Assignment:** 3 - Database Interaction  
**Submission Date:** November 8, 2025

## 📖 Assignment Overview

This project implements a Python-based student management system that demonstrates CRUD (Create, Read, Update, Delete) operations with a PostgreSQL database. Through this assignment, I learned how to:

- Connect Python applications to PostgreSQL databases
- Implement secure database queries using parameterized statements
- Handle database errors and exceptions
- Create user-friendly command-line interfaces
- Design and implement database schemas

## 🎯 Assignment Requirements Fulfilled

 **Database Schema Implementation**
- Created `students` table with exact specifications
- Implemented auto-increment primary key using SERIAL
- Added appropriate constraints (NOT NULL, UNIQUE)

 **Required Functions Implemented**
- `getAllStudents()` - Displays all student records in formatted table
- `addStudent()` - Inserts new student records with validation
- `updateStudentEmail()` - Updates email addresses with error handling
- `deleteStudent()` - Removes student records with confirmation prompts

 **Database Population**
- Inserted all 3 required initial student records
- Verified data integrity and constraints

 **Application Development**
- Built interactive command-line interface
- Implemented comprehensive error handling
- Added input validation for emails and dates
- Used parameterized queries for security

## 🎥 Video Demonstration

**[📺 Click here to view the application demo](https://your-video-link-here)**

The video demonstrates:
1. Database connection and initial data display
2. Adding a new student record
3. Updating an existing student's email
4. Deleting a student record
5. Error handling for invalid inputs

*Note: Please replace with actual video link after recording*

## 🏗️ Project Structure

```
Assignment-3-Database-Interaction/
├── src/
│   ├── main.py              # Main application with CRUD operations
│   ├── config.py            # Database configuration settings
│   └── database/
│       └── schema.sql       # Database schema and initial data
├── tests/
│   ├── test_crud.py         # CRUD operations testing script
│   └── verify_db.py         # Database connection verification
├── docs/
│   └── requirements.txt     # Python dependencies
├── README.md               # This documentation
└── .gitignore             # Git ignore file
```

## Setup and Installation Instructions

### Prerequisites

1. **Python 3.7+** installed on your system
2. **PostgreSQL** server installed and running
3. **pip** package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/ahmadbilal/Assignment-3-Database-Interaction.git
cd Assignment-3-Database-Interaction
```

### Step 2: Set Up Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r docs/requirements.txt
```

### Step 3: Database Setup

```bash
# Start PostgreSQL service (if not already running)
# macOS with Homebrew:
brew services start postgresql
# Linux:
sudo systemctl start postgresql

# Create database
psql -U postgres -c "CREATE DATABASE student_db;"

# Run schema file
psql -U postgres -d student_db -f src/database/schema.sql
```

### Step 4: Configure Database Connection

Edit `src/config.py` and update the database credentials:

```python
DB_CONFIG = {
    'host': 'localhost',
    'database': 'student_db', 
    'user': 'your_postgres_user',
    'password': 'your_password',
    'port': '5432'
}
```

## 🖥️ Running the Application

### Main Application
```bash
cd src
python3 main.py
```

### Testing CRUD Operations
```bash
cd tests
python3 test_crud.py
```

### Verify Database Connection
```bash
cd tests
python3 verify_db.py
```

## 📋 Application Features

### 1. View All Students (`getAllStudents()`)
- Retrieves all student records from database
- Displays data in formatted table with columns:
  - Student ID, First Name, Last Name, Email, Enrollment Date
- Handles empty database gracefully

### 2. Add New Student (`addStudent()`)
- Prompts for student information input
- Validates email format before insertion
- Validates date format (YYYY-MM-DD)
- Handles duplicate email constraint violations
- Returns auto-generated student ID

### 3. Update Student Email (`updateStudentEmail()`)
- Allows updating email for existing students
- Verifies student exists before update
- Validates new email format
- Prevents duplicate email addresses
- Shows before/after values for confirmation

### 4. Delete Student (`deleteStudent()`)
- Removes student records by ID
- Verifies student exists before deletion
- Requires user confirmation before deleting
- Displays deleted student information

## 🛡️ Security Features

- **SQL Injection Prevention**: Uses parameterized queries (`%s` placeholders)
- **Input Validation**: Validates email formats and date formats
- **Error Handling**: Comprehensive exception handling for database operations
- **Transaction Management**: Proper commit/rollback for database integrity
