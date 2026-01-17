# Python enumerate() Example with Strings

## Overview
This program demonstrates how the built-in Python function `enumerate()` works
when applied to a **string**. Since strings are iterable in Python, `enumerate()`
returns both the **index** and the **character** for each element in the string.

---

## Program Description
The script:
- Defines a string value
- Uses `enumerate()` to pair each character with its index
- Converts the result into a list for easy viewing
- Prints the indexed character list

---

## Code
```python
a = "Sudipto is the best"
senu = enumerate(a)

print(list(senu))
