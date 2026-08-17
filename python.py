students = []


def add_student():
    name = input("Enter student name: ")
    usn = input("Enter USN: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "usn": usn,
        "branch": branch,
        "marks": marks
    }

    students.append(student)
    print("\nStudent added successfully!")


def display_students():
    if not students:
        print("\nNo students found.")
        return

    print("\n----- Student List -----")

    for student in students:
        print(f"Name   : {student['name']}")
        print(f"USN    : {student['usn']}")
        print(f"Branch : {student['branch']}")
        print(f"Marks  : {student['marks']}")
        print("------------------------")


def search_student():
    usn = input("Enter USN to search: ")

    for student in students:
        if student["usn"] == usn:
            print("\nStudent Found!")
            print(f"Name   : {student['name']}")
            print(f"USN    : {student['usn']}")
            print(f"Branch : {student['branch']}")
            print(f"Marks  : {student['marks']}")
            return

    print("\nStudent not found.")


def calculate_average():
    if not students:
        print("\nNo student data available.")
        return

    total = sum(student["marks"] for student in students)
    average = total / len(students)

    print(f"\nClass Average: {average:.2f}")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Calculate Average")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            calculate_average()

        elif choice == "5":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()