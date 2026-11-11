"""Student Record Manager

A command-line program that collects student details (name, age, roll number,
marks), assigns a grade to each student, and prints a record list followed by
a pass/fail result summary.
"""

PASS_MARKS = 40


def get_grade(marks):
    """Return the grade for the given marks."""
    if marks > 95:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= PASS_MARKS:
        return "C"
    else:
        return "F"


def read_int(prompt, minimum=None):
    """Keep asking until the user enters a valid whole number."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}.")
            continue
        return value


def read_marks(prompt):
    """Keep asking until the user enters marks between 0 and 100."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if not 0 <= value <= 100:
            print("Marks must be between 0 and 100.")
            continue
        return value


def collect_student_data(number_of_students):
    """Collect details for each student and return them as a list of dicts."""
    student_data = []

    for i in range(number_of_students):
        print(f"Enter the details of student {i + 1}:")
        name = input("Enter the name of student: ").strip()
        age = read_int("Enter the age of student: ", minimum=1)
        roll_no = read_int("Enter the roll number of student: ", minimum=1)
        marks = read_marks("Enter the marks of student (0-100): ")

        student_data.append(
            {
                "name": name,
                "age": age,
                "rollno": roll_no,
                "marks": marks,
                "grade": get_grade(marks),
            }
        )
        print("Student data added successfully!\n")

    return student_data


def print_student_data(student_data):
    """Print the full record of every student."""
    print("Student Data: \n")
    for student in student_data:
        print(
            f"Name: {student['name']}, Age: {student['age']}, "
            f"Roll No: {student['rollno']}, Marks: {student['marks']}, "
            f"Grade: {student['grade']}"
        )


def print_results(student_data):
    """Print pass/fail results for every student."""
    print("\nStudent Results: \n")
    for student in student_data:
        if student["marks"] >= PASS_MARKS:
            print(
                f"Name: {student['name']}, Age: {student['age']}, "
                f"Roll No: {student['rollno']}, Marks: {student['marks']}, "
                f"Grade: {student['grade']}"
            )
        else:
            print(f"Name: {student['name']} has failed with Grade: {student['grade']}")


def main():
    number_of_students = read_int("Enter the number of students: ", minimum=1)
    student_data = collect_student_data(number_of_students)
    print_student_data(student_data)
    print_results(student_data)


if __name__ == "__main__":
    main()
