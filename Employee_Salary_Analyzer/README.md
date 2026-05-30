# Employee Salary Analyzer in Python

## Overview

This program analyzes employee salary data stored in a dictionary.

It identifies:
- The highest paid employee
- The lowest paid employee
- The average salary across all employees

The project demonstrates dictionary operations, aggregation, and simple business analytics.

---

## Code

```python
employees = {
    "John": 55000,
    "Alice": 72000,
    "Bob": 48000,
    "David": 81000
}

highest_paid = max(employees, key=employees.get)
lowest_paid = min(employees, key=employees.get)

average_salary = sum(employees.values()) / len(employees)

print("Highest Paid Employee:", highest_paid)
print("Salary:", employees[highest_paid])

print("\nLowest Paid Employee:", lowest_paid)
print("Salary:", employees[lowest_paid])

print("\nAverage Salary:", average_salary)
```

---

## How It Works

1. Employee names and salaries are stored in a dictionary
2. `max()` identifies the employee with the highest salary
3. `min()` identifies the employee with the lowest salary
4. `sum()` calculates the total salary amount
5. The average salary is calculated by dividing the total by the number of employees
6. Results are displayed in a readable format

---

## Example Output

```text
Highest Paid Employee: David
Salary: 81000

Lowest Paid Employee: Bob
Salary: 48000

Average Salary: 64000.0
```

---

## Concepts Covered

- Dictionaries
- max()
- min()
- sum()
- Aggregation
- Data analysis
- Business reporting

---

## Why This Program?

This project introduces real-world data analysis concepts such as:

- Employee record management
- Salary analytics
- Data summarization
- Decision-support reporting

These concepts are commonly used in:
- HR systems
- Payroll software
- Business dashboards
- Data analytics applications

---

## Possible Improvements

- Accept employee data from user input
- Store department information
- Find employees above average salary
- Generate salary reports
- Export results to a file

---

## Author

Daily Python Practice  
Employee Salary Analyzer
