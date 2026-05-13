# Find the Second Largest Number in a List – Python Program

## Overview
This program finds the second largest number in a list.
It demonstrates list manipulation, sorting, and duplicate removal using sets.

---

## Code
```python
numbers = [12, 45, 7, 89, 34, 89, 67]

unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Second largest number:", unique_numbers[-2])
