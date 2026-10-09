Student Management System

Overview

The Student Management System is a menu-driven command-line application developed using Python. It allows users to manage student records efficiently through basic CRUD operations and search functionality. Student data is stored in a JSON file so that records remain available after the application is closed.

Features

- Add Student: Create a student record with a unique ID, name, age, course, and email.
- View Students: Display all saved student records.
- Update Student: Modify an existing student's details.
- Delete Student: Delete a student record after confirmation.
- Search Students: Search records by student ID, name, course, or email.
- Input Validation: Reject empty fields, invalid ages, and incorrectly formatted email addresses.
- Exception Handling: Handle common input and file-reading errors.
- Persistent Storage: Store records in a JSON file.
- Modular Code: Separate application logic, validation, and storage into different Python modules.

Technologies Used

- Python 3
- JSON
- Python standard library

Project Structure

student-management-system/
├── main.py
├── crud.py
├── validation.py
├── storage.py
├── students.json
├── requirements.txt
├── README.md
├── DOCUMENTATION.md
└── .gitignore

Requirements

- Python 3 installed on your computer.
- A code editor or terminal to run the application.

No third-party Python packages are required.

Installation and Execution

1. Download or clone the repository.
2. Open a terminal in the project directory.
3. Run the application:

python main.py

On some Windows systems, use:

py main.py

How to Use

When the application starts, a menu appears:

1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Search Student
6. Exit

Enter the corresponding menu number and follow the prompts.

Data Storage

Student records are stored in "students.json". The application reads existing records when needed and writes changes to the file. The initial file should contain an empty JSON list:

[]

Keep "students.json" in the project directory. Do not replace existing records with "[]" after adding data unless you intend to clear the file.

Testing

Test all menu options, invalid inputs, searches with no matches, attempts to update or delete nonexistent IDs, and data persistence after restarting the program.

Version

Version: 1.0.0

Author

Developed as part of the Python Internship — Task 1.