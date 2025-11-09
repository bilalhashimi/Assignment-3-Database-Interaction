"""
Student Management System - PostgreSQL Database Application
COMP-3005-A-F Assignment 3: Database Interaction with PostgreSQL

This application demonstrates CRUD operations on a PostgreSQL database using Python.
I learned how to connect Python to PostgreSQL and implement all required database operations.

Student: Ahmad Bilal
Student ID: [Your Student ID]
Course: COMP-3005-A-F
Assignment: 3 - Database Interaction
Date: November 8, 2025

This was a great learning experience working with databases in Python!
"""

import psycopg2
from psycopg2 import sql, Error
from datetime import datetime
from config import DB_CONFIG, CONNECTION_TIMEOUT


class StudentDatabase:
    """
    A class to handle database operations for the student management system.
    I created this class to organize all my database functions in one place.
    This makes the code cleaner and easier to understand.
    """
    
    def __init__(self):
        """Initialize the database connection variables."""
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """
        Establish connection to the PostgreSQL database.
        Returns True if successful, False otherwise.
        """
        try:
            self.connection = psycopg2.connect(
                host=DB_CONFIG['host'],
                database=DB_CONFIG['database'],
                user=DB_CONFIG['user'],
                password=DB_CONFIG['password'],
                port=DB_CONFIG['port'],
                connect_timeout=CONNECTION_TIMEOUT
            )
            self.cursor = self.connection.cursor()
            print("✅ Successfully connected to PostgreSQL database")
            return True
        except Error as e:
            print(f"❌ Error connecting to PostgreSQL database: {e}")
            return False
    
    def disconnect(self):
        """Close the database connection and cursor."""
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            print("🔌 Database connection closed")
        except Error as e:
            print(f"❌ Error closing database connection: {e}")
    
    def getAllStudents(self):
        """
        Retrieves and displays all records from the students table.
        This function implements the READ operation of CRUD.
        I spent time making the output look nice and formatted.
        Returns a list of tuples containing student data.
        """
        try:
            # Execute SQL query to get all students - learned about ORDER BY for sorting
            query = "SELECT student_id, first_name, last_name, email, enrollment_date FROM students ORDER BY student_id;"
            self.cursor.execute(query)
            
            # Fetch all results
            students = self.cursor.fetchall()
            
            # Display results in a formatted way
            print("\n📊 All Students:")
            print("-" * 80)
            print(f"{'ID':<4} {'First Name':<15} {'Last Name':<15} {'Email':<25} {'Enrollment Date'}")
            print("-" * 80)
            
            if students:
                for student in students:
                    student_id, first_name, last_name, email, enrollment_date = student
                    print(f"{student_id:<4} {first_name:<15} {last_name:<15} {email:<25} {enrollment_date}")
            else:
                print("No students found in the database.")
            
            print("-" * 80)
            return students
            
        except Error as e:
            print(f"❌ Error retrieving students: {e}")
            return []
    
    def addStudent(self, first_name, last_name, email, enrollment_date):
        """
        Inserts a new student record into the students table.
        This is the CREATE operation in CRUD - I learned about INSERT statements.
        
        I had to figure out how to handle the auto-increment ID and return it.
        Also learned about handling unique constraint violations for email.
        
        Parameters:
        - first_name (str): Student's first name
        - last_name (str): Student's last name  
        - email (str): Student's email address (must be unique)
        - enrollment_date (str): Enrollment date in YYYY-MM-DD format
        
        Returns True if successful, False otherwise.
        """
        try:
            # Validate input parameters
            if not all([first_name, last_name, email]):
                print("❌ Error: First name, last name, and email are required")
                return False
            
            # SQL query to insert new student
            query = """
                INSERT INTO students (first_name, last_name, email, enrollment_date) 
                VALUES (%s, %s, %s, %s) RETURNING student_id;
            """
            
            # Execute the query with parameters
            self.cursor.execute(query, (first_name, last_name, email, enrollment_date))
            
            # Get the auto-generated student ID
            new_student_id = self.cursor.fetchone()[0]
            
            # Commit the transaction
            self.connection.commit()
            
            print(f"✅ Student added successfully with ID: {new_student_id}")
            print(f"   Name: {first_name} {last_name}")
            print(f"   Email: {email}")
            print(f"   Enrollment Date: {enrollment_date}")
            
            return True
            
        except psycopg2.IntegrityError as e:
            # Handle unique constraint violation (duplicate email)
            self.connection.rollback()
            print(f"❌ Error: Email '{email}' already exists in the database")
            return False
        except Error as e:
            # Handle other database errors
            self.connection.rollback()
            print(f"❌ Error adding student: {e}")
            return False
    
    def updateStudentEmail(self, student_id, new_email):
        """
        Updates the email address for a student with the specified student_id.
        
        Parameters:
        - student_id (int): The ID of the student to update
        - new_email (str): The new email address
        
        Returns True if successful, False otherwise.
        """
        try:
            # Validate input parameters
            if not new_email:
                print("❌ Error: New email address is required")
                return False
            
            # First, check if the student exists
            check_query = "SELECT first_name, last_name, email FROM students WHERE student_id = %s;"
            self.cursor.execute(check_query, (student_id,))
            student = self.cursor.fetchone()
            
            if not student:
                print(f"❌ Error: Student with ID {student_id} not found")
                return False
            
            # Get current student info
            old_first_name, old_last_name, old_email = student
            
            # SQL query to update email
            update_query = "UPDATE students SET email = %s WHERE student_id = %s;"
            
            # Execute the update query
            self.cursor.execute(update_query, (new_email, student_id))
            
            # Commit the transaction
            self.connection.commit()
            
            print(f"✅ Email updated successfully for student ID: {student_id}")
            print(f"   Student: {old_first_name} {old_last_name}")
            print(f"   Old Email: {old_email}")
            print(f"   New Email: {new_email}")
            
            return True
            
        except psycopg2.IntegrityError as e:
            # Handle unique constraint violation (duplicate email)
            self.connection.rollback()
            print(f"❌ Error: Email '{new_email}' already exists in the database")
            return False
        except Error as e:
            # Handle other database errors
            self.connection.rollback()
            print(f"❌ Error updating student email: {e}")
            return False
    
    def deleteStudent(self, student_id):
        """
        Deletes the record of the student with the specified student_id.
        
        Parameters:
        - student_id (int): The ID of the student to delete
        
        Returns True if successful, False otherwise.
        """
        try:
            # First, check if the student exists and get their info
            check_query = "SELECT first_name, last_name, email FROM students WHERE student_id = %s;"
            self.cursor.execute(check_query, (student_id,))
            student = self.cursor.fetchone()
            
            if not student:
                print(f"❌ Error: Student with ID {student_id} not found")
                return False
            
            # Get student info for confirmation message
            first_name, last_name, email = student
            
            # SQL query to delete the student
            delete_query = "DELETE FROM students WHERE student_id = %s;"
            
            # Execute the delete query
            self.cursor.execute(delete_query, (student_id,))
            
            # Commit the transaction
            self.connection.commit()
            
            print(f"✅ Student deleted successfully")
            print(f"   ID: {student_id}")
            print(f"   Name: {first_name} {last_name}")
            print(f"   Email: {email}")
            
            return True
            
        except Error as e:
            # Handle database errors
            self.connection.rollback()
            print(f"❌ Error deleting student: {e}")
            return False


def display_menu():
    """Display the main menu options for the application."""
    print("\n" + "=" * 50)
    print("🎓 STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. 📋 View All Students")
    print("2. ➕ Add New Student")
    print("3. ✏️  Update Student Email")
    print("4. 🗑️  Delete Student")
    print("5. 🚪 Exit")
    print("=" * 50)


def get_user_input():
    """Get and validate user input for menu selection."""
    try:
        choice = input("Enter your choice (1-5): ").strip()
        return choice
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        return '5'


def validate_email(email):
    """Basic email validation."""
    return '@' in email and '.' in email.split('@')[-1]


def validate_date(date_string):
    """Validate date format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def main():
    """
    Main function that runs the student management application.
    I designed this to be user-friendly with a menu-driven interface.
    
    This was my first time building a complete database application!
    I learned about error handling, user input validation, and database connections.
    """
    print("🚀 Starting Student Management System...")
    print("   Built by Ahmad Bilal for COMP-3005-A-F Assignment 3")
    
    # Create database instance
    db = StudentDatabase()
    
    # Attempt to connect to database
    if not db.connect():
        print("❌ Failed to connect to database. Please check your configuration.")
        return
    
    try:
        while True:
            display_menu()
            choice = get_user_input()
            
            if choice == '1':
                # View all students
                print("\n🔍 Retrieving all students...")
                db.getAllStudents()
                
            elif choice == '2':
                # Add new student
                print("\n➕ Adding New Student")
                print("-" * 30)
                
                first_name = input("Enter first name: ").strip()
                last_name = input("Enter last name: ").strip()
                email = input("Enter email: ").strip()
                enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ").strip()
                
                # Validate inputs
                if not all([first_name, last_name, email, enrollment_date]):
                    print("❌ All fields are required!")
                    continue
                
                if not validate_email(email):
                    print("❌ Invalid email format!")
                    continue
                
                if not validate_date(enrollment_date):
                    print("❌ Invalid date format! Use YYYY-MM-DD")
                    continue
                
                db.addStudent(first_name, last_name, email, enrollment_date)
                
            elif choice == '3':
                # Update student email
                print("\n✏️  Updating Student Email")
                print("-" * 30)
                
                try:
                    student_id = int(input("Enter student ID: ").strip())
                    new_email = input("Enter new email: ").strip()
                    
                    if not validate_email(new_email):
                        print("❌ Invalid email format!")
                        continue
                    
                    db.updateStudentEmail(student_id, new_email)
                    
                except ValueError:
                    print("❌ Invalid student ID! Please enter a number.")
                
            elif choice == '4':
                # Delete student
                print("\n🗑️  Deleting Student")
                print("-" * 30)
                
                try:
                    student_id = int(input("Enter student ID to delete: ").strip())
                    
                    # Confirmation prompt
                    confirm = input(f"Are you sure you want to delete student ID {student_id}? (y/N): ").strip().lower()
                    
                    if confirm == 'y' or confirm == 'yes':
                        db.deleteStudent(student_id)
                    else:
                        print("❌ Delete operation cancelled.")
                        
                except ValueError:
                    print("❌ Invalid student ID! Please enter a number.")
                
            elif choice == '5':
                # Exit application
                print("\n👋 Thank you for using Student Management System!")
                break
                
            else:
                print("❌ Invalid choice! Please enter a number between 1-5.")
            
            # Pause before showing menu again
            input("\nPress Enter to continue...")
    
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted by user. Goodbye!")
    
    finally:
        # Always close database connection
        db.disconnect()


if __name__ == "__main__":
    main()
