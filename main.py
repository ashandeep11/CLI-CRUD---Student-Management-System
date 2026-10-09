from crud import (
    create_student,
    read_students,
    update_student,
    delete_student,
    search_students
)

from storage import initialize_storage

def display_menu():
    print("\n" + "-" * 60)
    print("Student Management System")
    print("-" * 60)
    print("1. Create Student")
    print("2. Read Students")
    print("3. Update Student")
    print("4. Delete Students")
    print("5. Search Students")
    print("6. Exit")
    print("-" * 60)

def main():
    initialize_storage()

    while True:
        display_menu()
        choice=input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                create_student()

            elif choice == "2":
                read_students()

            elif choice == "3":
                update_student()

            elif choice == "4":
                delete_student()

            elif choice == "5":
                search_students()

            elif choice == "6":
                print("\n thanks for using our Student Management System. GOODBYE!!")
                break

            else:
                print ("\n Invalid choice!! Please enter a valid number (1-6)")

        except Exception as error:
            print(f"\n An unexpected error occurred: {error}")

if __name__ == "__main__":
    main()
