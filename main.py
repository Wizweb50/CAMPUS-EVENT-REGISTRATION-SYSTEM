
from student import Student
from registration import RegistrationManager


def main():
    manager = RegistrationManager()

    while True:
        print("\n===== Campus Event Registration =====")
        print("1. Register Student")
        print("2. Display Participants")
        print("3. Search Registration")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            reg_no = input("Enter registration number: ")
            workshop = input("Enter workshop name: ")

            student = Student(name, reg_no, workshop)

            result = manager.register_student(student)
            print(result)

        elif choice == "2":
            manager.display_participants()

        elif choice == "3":
            reg_no = input("Enter registration number to search: ")

            student = manager.search_student(reg_no)

            if student:
                print("\nRegistration Found!")
                print(student.display())
            else:
                print("\nError: No registration found.")

        elif choice == "4":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
