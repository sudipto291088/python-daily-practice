# Find Duplicate Elements in a List – Python Program

## Overview
This program finds duplicate elements in a list using loops and conditional logic.
It demonstrates list traversal, counting occurrences, and avoiding repeated duplicate entries.

---

## Code
```python
numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate elements:", duplicates)
