# Find Common Elements Between Two Lists – Python Program

## Overview
This program finds the common elements shared between two lists.
It demonstrates list traversal, membership checking, and conditional logic in Python.

---

## Code
```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = []

for item in list1:
    if item in list2:
        common.append(item)

print("Common elements:", common)
