# Employee Performance Dashboard in Python

## Overview

This program analyzes employee performance scores and generates a summary report.

The application:
- Calculates average performance
- Identifies the top performer
- Classifies employees as above or below average
- Generates a performance dashboard

The project demonstrates dictionaries, loops, conditional logic, and basic analytics.

---

## Code

```python
employees = {
    "John": 85,
    "Alice": 92,
    "Bob": 74,
    "David": 88,
    "Emma": 95
}

average_score = sum(employees.values()) / len(employees)

top_performer = max(employees, key=employees.get)

print("Employee Performance Report")
print("-" * 30)

for employee, score in employees.items():
    status = "Above Average" if score > average_score else "Below Average"

    print(f"{employee}: {score} ({status})")

print("\nAverage Score:", round(average_score, 2))
print("Top Performer:", top_performer)
```

---

## How It Works

1. Employee scores are stored in a dictionary
2. Average performance is calculated
3. The highest-performing employee is identified
4. Each employee is compared against the average
5. A performance report is generated

---

## Example Output

```text
Employee Performance Report
------------------------------

John: 85 (Below Average)
Alice: 92 (Above Average)
Bob: 74 (Below Average)
David: 88 (Above Average)
Emma: 95 (Above Average)

Average Score: 86.8
Top Performer: Emma
```

---

## Concepts Covered

- Dictionaries
- Loops
- Conditional expressions
- Aggregation functions
- Data analysis

---

## Why This Program?

This project introduces:

- Performance analytics
- Business reporting
- KPI evaluation
- Workforce analytics

These concepts are commonly used in:

- HR dashboards
- Employee review systems
- Business intelligence tools
- Performance management software

---

## Possible Improvements

- Add departments
- Rank employees
- Generate charts
- Store data in CSV files
- Create monthly reports

---

## Author

Daily Python Practice  
Employee Performance Dashboard
