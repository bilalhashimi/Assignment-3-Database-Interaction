#!/usr/bin/env python3
"""
Quick database connection verification script
COMP-3005-A-F Assignment 3

I created this to quickly check if my database setup is working.
Very useful for troubleshooting connection issues!

Student: Ahmad Bilal
"""

import sys
import os
# Add parent directory to path so we can import from src
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from config import DB_CONFIG
import psycopg2
from psycopg2 import Error

def verify_connection():
    """Verify database connection and show basic info"""
    try:
        print("🔍 Verifying database connection...")
        print(f"📍 Host: {DB_CONFIG['host']}")
        print(f"📂 Database: {DB_CONFIG['database']}")
        print(f"👤 User: {DB_CONFIG['user']}")
        print(f"🔌 Port: {DB_CONFIG['port']}")
        print()
        
        # Test connection
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Get PostgreSQL version
        cursor.execute('SELECT version();')
        db_version = cursor.fetchone()[0]
        print(f"✅ Connection successful!")
        print(f"🗄️  PostgreSQL version: {db_version.split(',')[0]}")
        
        # Check students table
        cursor.execute('SELECT COUNT(*) FROM students;')
        student_count = cursor.fetchone()[0]
        print(f"👥 Students in database: {student_count}")
        
        # Check table structure
        cursor.execute("""
            SELECT column_name, data_type, is_nullable 
            FROM information_schema.columns 
            WHERE table_name = 'students' 
            ORDER BY ordinal_position;
        """)
        columns = cursor.fetchall()
        
        print("\n📋 Table Structure:")
        print("-" * 40)
        for col_name, data_type, is_nullable in columns:
            nullable = "NULL" if is_nullable == "YES" else "NOT NULL"
            print(f"  {col_name:<15} {data_type:<10} {nullable}")
        
        conn.close()
        print("\n🎉 Database is ready for use!")
        return True
        
    except Error as e:
        print(f"❌ Connection failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    verify_connection()
