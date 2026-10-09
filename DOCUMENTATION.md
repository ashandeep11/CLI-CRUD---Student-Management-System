Technical Documentation — Student Management System

1. Introduction

The Student Management System is a command-line application written in Python. It provides functionality to create, view, update, delete, and search student records. JSON is used for persistent data storage.

2. Objectives

- Practise Python functions, lists, and dictionaries.
- Implement CRUD operations.
- Store and retrieve structured data using JSON.
- Validate user input and handle common errors.
- Organize code into reusable modules.

3. System Requirements

- Python 3
- A terminal or command prompt
- A code editor such as Visual Studio Code

The application uses Python's standard library and does not require external packages.

4. Module Descriptions

"main.py"

- Displays the application menu.
- Receives the user's menu selection.
- Calls the appropriate function from "crud.py".
- Handles unexpected exceptions at the menu level.
- Starts the application through the "main()" function.

"crud.py"

Implements the application's main operations:

- "create_student()" — creates and saves a student record.
- "read_students()" — displays all student records.
- "update_student()" — updates an existing record.
- "delete_student()" — removes a record after confirmation.
- "search_students()" — searches records using a keyword.
- "get_next_id()" — generates the next student ID based on existing records.

"validation.py"

Contains helper functions for user input:

- "get_non_empty()" — rejects empty text.
- "get_positive_integer()" — accepts positive whole numbers.
- "get_valid_email()" — performs a basic email-format check.
- "get_optional_value()" — keeps the existing value if the user presses Enter.

"storage.py"

- Creates the JSON file if it does not exist.
- Loads student records from JSON.
- Saves updated records to JSON.
- Handles common file-reading and JSON-decoding errors.

"students.json"

Stores the student records as a JSON list. Each student record contains an ID, name, age, course, and email.

5. Data Model

Each student is represented as a Python dictionary with the following fields:

Field| Type| Description
"id"| Integer| Unique student identifier
"name"| String| Student's name
"age"| Integer| Student's age
"course"| String| Student's course
"email"| String| Student's email address

Multiple student dictionaries are stored in a list.

6. Application Workflow

1. The user starts the program using "python main.py".
2. The application initializes JSON storage.
3. The menu is displayed.
4. The user selects an operation.
5. The relevant function validates input and performs the operation.
6. Changes are saved to "students.json".
7. The menu is displayed again until the user selects Exit.

7. Data Persistence

The Python "json" module is used to serialize student records and store them in a file. "json.load()" reads records, while "json.dump()" writes records. This allows the records to remain available after the application closes, provided the JSON file is preserved.

8. Validation and Error Handling

The application checks that required text fields are not empty, age values are positive whole numbers, and email addresses meet a basic formatting check. It also handles common invalid inputs, missing files, and malformed JSON during loading.

The email check is basic and does not verify whether an email address actually exists.

9. Testing Checklist

- Add a student with valid details.
- View saved student records.
- Update a student's details.
- Delete a student after confirmation.
- Search using an ID, name, course, and email.
- Try invalid ages, empty text fields, and incorrectly formatted emails.
- Try searching for a nonexistent student.
- Try updating or deleting a nonexistent ID.
- Restart the program and confirm that saved records remain available.

Record the actual test results before submission.

10. Limitations

- The application runs in a terminal and does not have a graphical interface.
- JSON is suitable for this small project but is not intended for concurrent multi-user access.
- Email validation checks formatting only.
- Data is stored locally in a file.

11. Conclusion

This project demonstrates Python functions, modular programming, CRUD operations, input validation, exception handling, searching, and persistent storage using JSON.

Version: 1.0.0