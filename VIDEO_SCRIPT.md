# Video Demonstration Script
## COMP-3005-A-F Assignment 3: Student Management System

**Duration: 4-5 minutes**  
**Student: Ahmad Bilal**

### Video Outline:

#### Introduction (30 seconds)
- "Hello, I'm Ahmad Bilal, and this is my demonstration of Assignment 3 for COMP-3005-A-F"
- "I've implemented a Student Management System using Python and PostgreSQL"
- "Today I'll show you all the CRUD operations working with the database"

#### 1. Show Initial Setup (1 minute)
- Navigate to project directory
- Show project structure: src/, tests/, docs/
- Activate virtual environment: `source venv/bin/activate`
- Verify database connection: `cd tests && python3 verify_db.py`
- Show initial 3 student records in database

#### 2. Demonstrate getAllStudents() (30 seconds)
- Run main application: `cd src && python3 main.py`
- Select option 1 to view all students
- Show formatted table with John, Jane, and Jim
- Explain this demonstrates the READ operation

#### 3. Demonstrate addStudent() (1 minute)
- Select option 2 to add a new student
- Enter details:
  - First Name: Sarah
  - Last Name: Wilson  
  - Email: sarah.wilson@example.com
  - Enrollment Date: 2023-09-20
- Show success message with auto-generated ID
- View all students again to confirm addition

#### 4. Demonstrate updateStudentEmail() (45 seconds)
- Select option 3 to update student email
- Enter Sarah's student ID (should be 4)
- Update email to: s.wilson@example.com
- Show confirmation with old/new email values
- View all students to confirm update

#### 5. Demonstrate deleteStudent() (45 seconds)
- Select option 5 to delete student
- Enter Sarah's student ID
- Confirm deletion when prompted
- Show deleted student information
- View all students to confirm removal (back to original 3)

#### 6. Show Error Handling (45 seconds)
- Try to add student with duplicate email
- Show error message for unique constraint violation
- Try to update non-existent student ID
- Show appropriate error handling

#### Conclusion (30 seconds)
- "This completes the demonstration of all CRUD operations"
- "All assignment requirements have been fulfilled"
- "The application handles errors gracefully and validates user input"
- "Thank you for watching!"

### Recording Tips:
1. Use clean terminal with good font size
2. Speak clearly and explain what you're doing
3. Show actual database changes happening
4. Keep steady pace - not too fast or slow
5. Ensure all text is readable in recording

### Equipment Needed:
- Screen recording software (QuickTime, OBS, etc.)
- Clear audio (built-in mic should be fine)
- Good lighting for webcam if including face

### Upload Instructions:
1. Record video following the script above
2. Upload to YouTube as unlisted video
3. Update README.md with actual video link
4. Test the link works before submission
