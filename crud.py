from storage import load_students, save_students
from validation import(
    get_non_empty,
    get_positive_integer,
    get_valid_email,
    get_optional_value
)

def get_next_id(students):
    if not students:
        return 1
    else:
        return max(student['id'] for student in students) + 1

# Create a new student--------------------------------------------------------------------
def create_student():
        students = load_students()

        print("\n Add a new student : ")

        name = get_non_empty("Enter Student Name:")
        age = get_positive_integer("Enter Student Age:")
        course = get_non_empty("Enter Student Course:")
        email = get_valid_email("Enter Student Email:")

        student = {
            "id": get_next_id(students),
            "name": name,
            "age": age,
            "course": course,
            "email": email
        }
        students.append(student)
        save_students(students)
        print(f"\n Student {name} added successfully!")   
        print(f"Student id : {student['id']}")


# Read all students--------------------------------------------------------------------
def read_students():
        students = load_students()

        print("\n All students : ")

        if not students:
            print("No students record found.")
        else:
            for student in students:
                print(
                    f'''ID: {student['id']}, 
                    Name: {student['name']}, 
                    Age: {student['age']}, 
                    Course: {student['course']}, 
                    Email: {student['email']}'''
                    )


# Update a student--------------------------------------------------------------------
def update_student():
    students = load_students()

    if not students:
        print("\n No students record found.")
        return

    print("\n Update a student : ")

    student_id = get_positive_integer("Enter Student ID to update:")

    student = next((s for s in students if s['id'] == student_id), None)

    if student is None:
        print(f"\n Student with ID {student_id} not found.")
        return

    print("\nPress enter to keep the current value. Enter new value to update.")

    #update name
    student['name'] = get_optional_value("Enter Student Name:", student['name'])
        
    #update age
    while True:
        age_input = input(f"Enter Student Age [{student['age']}]: ").strip()
                
        if not age_input: 
            break
        
        try:
            age = int(age_input)
                    
            if age  > 0:
                student['age'] = age
                break
            else:
                print("Age must be a positive integer. Please try again.")

        except ValueError:
                print("Invalid input. Please enter a valid positive integer for age.")

        #update course
        student['course'] = get_optional_value("Enter Student Course:", student['course'])
        #update email
        while True:
            email_input = input(f"Enter Student Email [{student['email']}]: ").strip()
                
            if not email_input: 
             break

            if "@" in email_input and "." in email_input.split("@")[-1] and " " not in email_input:
                student['email'] = email_input
                break
            else:
                print("Invalid email format. Please try again.")

    save_students(students)
    print(f"\n Student with ID {student_id} updated successfully!")

# Delete a student---------------------------------------------------------------------

def delete_student():
    students = load_students()

    if not students:
        print("\nNo student records found.")
        return

    print("\n--- Delete Student ---")

    student_id = get_positive_integer(
        "Enter student ID: "
    )

    student = next(
        (s for s in students if s["id"] == student_id),
        None
    )

    if student is None:
        print("Student not found.")
        return

    confirm = input(
        f"Delete {student['name']} "
        f"(ID {student['id']})? (y/n): "
    ).strip().lower()

    if confirm == "y":
        students.remove(student)

        save_students(students)

        print("\nStudent deleted successfully!")

    else:
        print("\nDelete operation cancelled.")

#Search students---------------------------------------------------------------------

def search_students():
    students = load_students()

    if not students:
        print("\nNo student records found.")
        return

    print("\n--- Search Student ---")

    keyword = get_non_empty(
        "Enter name, course, email, or ID to search: "
    ).lower()

    matches = []

    for student in students:

        searchable = " ".join(
            [
                str(student["id"]),
                student["name"],
                student["course"],
                student["email"]
            ]
        ).lower()

        if keyword in searchable:
            matches.append(student)

    if not matches:
        print("\nNo matching students found.")
        return

    print(
        f"\nFound {len(matches)} matching record(s):"
    )

    for student in matches:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']} | "
            f"Email: {student['email']}"
        )