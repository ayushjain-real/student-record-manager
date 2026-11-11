# Student Record Manager

A command-line Python program that collects student details, assigns each student a grade based on marks, and prints a full record list followed by a pass/fail result summary.

## Features

- Accepts any number of students at runtime
- Stores each student's name, age, roll number, marks and grade
- Automatic grade assignment using fixed marks bands
- Input validation: rejects text where numbers are expected and marks outside 0-100, then asks again
- Separate pass/fail result report (pass mark: 40)
- Modular code: small functions for grading, input handling and printing

## Grading Scale

| Marks      | Grade |
|------------|-------|
| Above 95   | A+    |
| 80 - 95    | A     |
| 60 - 79.99 | B     |
| 40 - 59.99 | C     |
| Below 40   | F (fail) |

## Tech Stack

- Python 3.8+ (standard library only, no external packages)
- Concepts used: lists, dictionaries, functions, loops, conditionals, f-strings, input validation with `try/except`

## How to Run

1. Make sure Python 3.8 or higher is installed:
   ```bash
   python --version
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/ayushjain-real/student-record-manager.git
   cd student-record-manager
   ```
3. Run the program:
   ```bash
   python student_record_manager.py
   ```
   On some systems use `python3` instead of `python`.

## Sample Session

```
Enter the number of students: 3
Enter the details of student 1:
Enter the name of student: Aarav Shah
Enter the age of student: 20
Enter the roll number of student: 101
Enter the marks of student (0-100): 97.5
Student data added successfully!

Enter the details of student 2:
Enter the name of student: Riya Patel
Enter the age of student: 19
Enter the roll number of student: abc
Invalid input. Please enter a whole number.
Enter the roll number of student: 102
Enter the marks of student (0-100): 72
Student data added successfully!

Enter the details of student 3:
Enter the name of student: Kabir Mehta
Enter the age of student: 21
Enter the roll number of student: 103
Enter the marks of student (0-100): 35
Student data added successfully!

Student Data:

Name: Aarav Shah, Age: 20, Roll No: 101, Marks: 97.5, Grade: A+
Name: Riya Patel, Age: 19, Roll No: 102, Marks: 72.0, Grade: B
Name: Kabir Mehta, Age: 21, Roll No: 103, Marks: 35.0, Grade: F

Student Results:

Name: Aarav Shah, Age: 20, Roll No: 101, Marks: 97.5, Grade: A+
Name: Riya Patel, Age: 19, Roll No: 102, Marks: 72.0, Grade: B
Name: Kabir Mehta has failed with Grade: F
```

## Project Structure

```
student-record-manager/
├── student_record_manager.py   # main program
├── requirements.txt            # dependencies (none required)
├── README.md                   # project documentation
├── LICENSE                     # MIT license
└── .gitignore                  # files Git should ignore
```

## Possible Improvements

- Save and load records from a CSV or JSON file
- Add search by roll number and sorting by marks
- Show class statistics (average, highest, lowest, pass percentage)
- Prevent duplicate roll numbers
- Add unit tests for the grading function

## Author

**Ayush**

ECE graduate (B.Tech, 2023) building skills in Python, data analysis and machine learning.

GitHub: [ayushjain-real](https://github.com/ayushjain-real) | LinkedIn: [Ayush Jain](https://www.linkedin.com/in/ayush-jain-b02863416/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
