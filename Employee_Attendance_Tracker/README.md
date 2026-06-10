# Employee Attendance Tracker in Python

## Overview

This program tracks employee attendance and generates a simple attendance report.

The application:
- Stores employee attendance records
- Counts present employees
- Counts absent employees
- Calculates attendance percentage

The project demonstrates dictionaries, loops, conditional logic, and reporting techniques.

---

## Code

```python
attendance = {
    "John": "Present",
    "Alice": "Absent",
    "Bob": "Present",
    "David": "Present",
    "Emma": "Absent"
}

present_count = 0
absent_count = 0

for employee, status in attendance.items():
    if status == "Present":
        present_count += 1
    else:
        absent_count += 1

attendance_percentage = (present_count / len(attendance)) * 100

print("Present Employees:", present_count)
print("Absent Employees:", absent_count)
print("Attendance Percentage:", round(attendance_percentage, 2), "%")
```

---

## How It Works

1. Employee attendance records are stored in a dictionary
2. The program loops through all employees
3. Attendance counts are calculated
4. Attendance percentage is computed
5. Results are displayed as a summary report

---

## Example Output

```text
Present Employees: 3
Absent Employees: 2
Attendance Percentage: 60.0 %
```

---

## Concepts Covered

- Dictionaries
- Loops
- Conditional statements
- Percentage calculations
- Reporting logic

---

## Why This Program?

This project introduces:

- Workforce reporting
- Attendance monitoring
- Business metrics
- Data summarization

These concepts are commonly used in:

- HR systems
- Employee management software
- School attendance systems
- Business dashboards

---

## Possible Improvements

- Accept attendance from user input
- Track attendance by date
- Generate monthly attendance reports
- Export reports to CSV
- Visualize attendance trends

---

## Author

Daily Python Practice  
Employee Attendance Tracker
