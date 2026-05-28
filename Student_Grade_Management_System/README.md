
## Overview
This program is a simple student grade management system built using Python dictionaries.
It stores student names, marks, and grades, then displays a formatted student report.

The project demonstrates nested dictionaries, loops, conditional logic,
and structured data management.

---

## Code
```python
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "F"

    students[name] = {
        "Marks": marks,
        "Grade": grade
    }

print("\nStudent Report:")

for name, details in students.items():
    print(f"{name} -> Marks: {details['Marks']}, Grade: {details['Grade']}")
