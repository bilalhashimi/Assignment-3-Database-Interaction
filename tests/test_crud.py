#!/usr/bin/env python3
"""
Test script to demonstrate all CRUD operations
COMP-3005-A-F Assignment 3

This script tests all the database functions I implemented.
It's really helpful for making sure everything works correctly!

Student: Ahmad Bilal
"""

import sys
import os
# Add parent directory to path so we can import from src
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import StudentDatabase
from datetime import date

def test_crud_operations():
    """Test all CRUD operations"""
    print("🧪 Testing Student Database CRUD Operations")
    print("=" * 50)
    
    # Initialize database connection
    db = StudentDatabase()
    
    if not db.connect():
        print("❌ Failed to connect to database")
        return
    
    try:
        # Test 1: View all students (READ)
        print("\n1️⃣ Testing getAllStudents():")
        db.getAllStudents()
        
        # Test 2: Add a new student (CREATE)
        print("\n2️⃣ Testing addStudent():")
        success = db.addStudent(
            "Alice", 
            "Johnson", 
            "alice.johnson@example.com", 
            "2023-09-15"
        )
        if success:
            print("✅ Student added successfully!")
        
        # Show updated list
        print("\n📋 Updated student list:")
        db.getAllStudents()
        
        # Test 3: Update student email (UPDATE)
        print("\n3️⃣ Testing updateStudentEmail():")
        # First, get the new student's ID
        db.cursor.execute("SELECT student_id FROM students WHERE email = 'alice.johnson@example.com';")
        result = db.cursor.fetchone()
        if result:
            student_id = result[0]
            success = db.updateStudentEmail(student_id, "alice.j.new@example.com")
            if success:
                print("✅ Email updated successfully!")
        
        # Show updated list
        print("\n📋 Updated student list after email change:")
        db.getAllStudents()
        
        # Test 4: Delete a student (DELETE)
        print("\n4️⃣ Testing deleteStudent():")
        if result:
            success = db.deleteStudent(student_id)
            if success:
                print("✅ Student deleted successfully!")
        
        # Show final list
        print("\n📋 Final student list:")
        db.getAllStudents()
        
        print("\n🎉 All CRUD operations tested successfully!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
    
    finally:
        db.disconnect()

if __name__ == "__main__":
    test_crud_operations()
