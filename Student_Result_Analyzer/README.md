# Student Result Analyzer in Python

## Overview

This program analyzes student marks and generates a summary report.

The application:
- Calculates average marks
- Finds the class topper
- Counts passed students
- Counts failed students

The project demonstrates dictionaries, loops, aggregation functions, and educational data analysis.

---

## Code

```python
students = {
    "John": 78,
    "Alice": 92,
    "Bob": 65,
    "David": 55,
    "Emma": 88
}

total_marks = sum(students.values())
average_marks = total_marks / len(students)

topper = max(students, key=students.get)

passed = 0
failed = 0

for marks in students.values():
    if marks >= 60:
        passed += 1
    else:
        failed += 1

print("Average Marks:", round(average_marks, 2))
print("Topper:", topper)
print("Passed Students:", passed)
print("Failed Students:", failed)
```

---

## How It Works

1. Student names and marks are stored in a dictionary
2. The average score is calculated
3. The student with the highest marks is identified
4. The program counts pass and fail records
5. A summary report is displayed

---

## Example Output

```text
Average Marks: 75.6
Topper: Alice
Passed Students: 4
Failed Students: 1
```

---

## Concepts Covered

- Dictionaries
- Loops
- sum()
- max()
- Conditional statements
- Data analysis

---

## Why This Program?

This project introduces:

- Educational analytics
- Student performance tracking
- Reporting systems
- Summary statistics

These concepts are commonly used in:

- School management systems
- Learning platforms
- Academic dashboards
- Educational reporting tools

---

## Possible Improvements

- Add subject-wise marks
- Calculate grades automatically
- Generate ranking lists
- Store results in a file
- Create report cards

---

## Author

Daily Python Practice  
Student Result Analyzer
