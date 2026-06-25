# Student Attendance Dashboard in Python

## Overview

This project simulates a simple student attendance dashboard.

Each student has an attendance record represented by:
- **1** → Present
- **0** → Absent

The program calculates attendance statistics for every student and generates a summary report.

---

## Features

- Stores attendance records using dictionaries and lists
- Calculates total days present
- Computes attendance percentage
- Generates a formatted attendance report

---

## Code

```python
students = {
    "John": [1, 1, 0, 1, 1],
    "Alice": [1, 1, 1, 1, 1],
    "Bob": [0, 1, 0, 1, 0],
    "David": [1, 0, 1, 1, 1]
}

print("Attendance Report")
print("-" * 35)

for student, attendance in students.items():
    present = sum(attendance)
    percentage = (present / len(attendance)) * 100

    print(f"{student}")
    print(f"Days Present : {present}")
    print(f"Attendance   : {percentage:.1f}%")
    print("-" * 35)
```

---

## How It Works

1. Student attendance is stored in a dictionary.
2. Each value is a list containing attendance records.
3. The program loops through each student.
4. `sum()` counts the number of present days.
5. Attendance percentage is calculated.
6. A report is displayed for every student.

---

## Example Output

```text
Attendance Report
-----------------------------------

John
Days Present : 4
Attendance   : 80.0%

-----------------------------------

Alice
Days Present : 5
Attendance   : 100.0%

-----------------------------------

Bob
Days Present : 2
Attendance   : 40.0%

-----------------------------------

David
Days Present : 4
Attendance   : 80.0%
```

---

## Concepts Covered

- Dictionaries
- Lists
- Nested data structures
- Loops
- sum()
- Percentage calculation
- Formatted output

---

## Why This Project?

This project demonstrates how attendance data can be processed and summarized programmatically.

Similar techniques are widely used in:

- School Management Systems
- HR Attendance Systems
- Employee Time Tracking
- Analytics Dashboards

---

## Possible Improvements

- Accept attendance from user input
- Store attendance by date
- Highlight students below 75% attendance
- Export reports to CSV
- Generate attendance charts

---

## Author

Daily Python Practice

Student Attendance Dashboard
