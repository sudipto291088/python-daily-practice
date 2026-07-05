# Employee Data Summary in Python

## Overview

This program analyzes employee records stored as a list of dictionaries.

The application:
- Calculates the average salary
- Finds the oldest employee
- Generates a summary report

This project demonstrates how structured records can be processed without using external libraries such as Pandas.

---

## Code

```python
employees = [
    {"Name": "John", "Age": 28, "Salary": 55000},
    {"Name": "Alice", "Age": 35, "Salary": 72000},
    {"Name": "Bob", "Age": 30, "Salary": 48000},
    {"Name": "David", "Age": 42, "Salary": 81000}
]

total_salary = 0
oldest_employee = employees[0]

for employee in employees:
    total_salary += employee["Salary"]

    if employee["Age"] > oldest_employee["Age"]:
        oldest_employee = employee

average_salary = total_salary / len(employees)

print("Employee Summary")
print("-" * 30)

print("Average Salary:", average_salary)
print("Oldest Employee:", oldest_employee["Name"])
print("Highest Age:", oldest_employee["Age"])
```

---

## How It Works

1. Employee records are stored as a list of dictionaries.
2. The program loops through every employee.
3. Total salary is accumulated.
4. The oldest employee is identified.
5. Average salary is calculated.
6. A summary report is displayed.

---

## Example Output

```text
Employee Summary
------------------------------
Average Salary: 64000.0
Oldest Employee: David
Highest Age: 42
```

---

## Concepts Covered

- Lists
- Dictionaries
- Nested data structures
- Loops
- Data aggregation
- Basic analytics

---

## Why This Program?

This project introduces:

- Structured record processing
- Manual data analysis
- Summary statistics
- Business reporting

These concepts are commonly used in:

- Data preprocessing
- HR analytics
- Reporting systems
- Data Science workflows

---

## Possible Improvements

- Read employee data from a CSV file
- Find the highest salary
- Sort employees by salary
- Filter employees by age
- Export summary reports

---

## Author

Daily Python Practice

Employee Data Summary
