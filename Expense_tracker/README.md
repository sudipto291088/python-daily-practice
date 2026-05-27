# Simple Expense Tracker in Python

## Overview
This program is a basic expense tracker built using Python dictionaries.
It allows users to enter expense names and amounts, then calculates
the total expense.

The project demonstrates dictionaries, loops, user input handling,
and basic financial data processing.

---

## Code
```python
expenses = {}

n = int(input("How many expenses do you want to enter? "))

for i in range(n):
    item = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses[item] = amount

total = sum(expenses.values())

print("\nExpense Summary:")

for item, amount in expenses.items():
    print(f"{item} : ${amount}")

print(f"\nTotal Expense: ${total}")
