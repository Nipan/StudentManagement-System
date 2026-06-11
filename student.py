
def add_student(students):
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")

    students.append({
        "roll": roll,
        "name": name,
        "dept": dept
    })

    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 40)

    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Department: {s['dept']}")


def search_student(students):
    roll = input("Enter Roll Number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found")
            print(f"Roll: {s['roll']}")
            print(f"Name: {s['name']}")
            print(f"Department: {s['dept']}")
            return

    print("Student not found.")


def delete_student(students):
    roll = input("Enter Roll Number to delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully.")
            return

    print("Student not found.")
