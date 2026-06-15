# Employee Leave Management System in Python

## Overview

This program simulates a simple employee leave management system.

The application:
- Stores employee leave balances
- Accepts leave requests
- Validates leave availability
- Updates remaining leave balances

The project demonstrates dictionaries, conditional logic, user input handling, and HR-style workflow management.

---

## Code

```python
employees = {
    "John": 10,
    "Alice": 15,
    "Bob": 8
}

name = input("Enter employee name: ")

if name in employees:
    requested_days = int(input("Enter leave days requested: "))

    if requested_days <= employees[name]:
        employees[name] -= requested_days
        print("Leave Approved")
        print("Remaining Leave Balance:", employees[name])
    else:
        print("Insufficient Leave Balance")
else:
    print("Employee Not Found")
```

---

## How It Works

1. Employee leave balances are stored in a dictionary
2. The user enters an employee name
3. The employee's leave balance is checked
4. The requested leave days are validated
5. If sufficient leave is available:
   - Leave is approved
   - Remaining balance is updated
6. Otherwise, the request is rejected

---

## Example Run

### Input

```text
Enter employee name: Alice
Enter leave days requested: 5
```

### Output

```text
Leave Approved
Remaining Leave Balance: 10
```

---

## Concepts Covered

- Dictionaries
- Conditional statements
- User input handling
- Data validation
- Business rules

---

## Why This Program?

This project introduces:

- HR workflow automation
- Resource allocation
- Validation logic
- Employee record management

These concepts are commonly used in:

- HR management systems
- Employee portals
- Leave tracking software
- Enterprise applications

---

## Possible Improvements

- Add new employees
- Track leave history
- Different leave types (sick, vacation, personal)
- Save records to a file
- Generate leave reports

---

## Author

Daily Python Practice  
Employee Leave Management System
