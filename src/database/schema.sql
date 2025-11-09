-- PostgreSQL Database Schema for Student Management System
-- COMP-3005-A-F Assignment 3: Database Interaction
-- Student: Ahmad Bilal
-- Date: November 8, 2025

-- This file contains the table definitions and initial data for the students table
-- I learned how to create tables with constraints and insert initial data

-- Drop table if exists (for clean setup)
DROP TABLE IF EXISTS students;

-- Create students table with specified schema
-- I learned about SERIAL for auto-increment and constraints
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,           -- Auto-increment primary key (learned about SERIAL)
    first_name TEXT NOT NULL,                -- Student's first name (required)
    last_name TEXT NOT NULL,                 -- Student's last name (required)  
    email TEXT NOT NULL UNIQUE,              -- Student's email (required and unique constraint)
    enrollment_date DATE                     -- Date when student enrolled
);

-- Insert initial data into students table
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

-- Display confirmation of data insertion
SELECT 'Initial data inserted successfully' AS status;

-- Show all inserted records
SELECT * FROM students ORDER BY student_id;
