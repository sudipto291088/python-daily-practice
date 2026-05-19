# Find Missing Number in a Sequence – Python Program

## Overview
This program finds the missing number in a sequence of integers.
It demonstrates mathematical problem solving using formulas and list operations in Python.

---

## Code
```python
numbers = [1, 2, 3, 5, 6]

n = max(numbers)

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

missing_number = expected_sum - actual_sum

print("Missing number is:", missing_number)
