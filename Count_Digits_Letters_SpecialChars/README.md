# Count Digits, Letters, and Special Characters in Python

## Overview
This program counts the number of letters, digits, and special characters in a string.
It demonstrates character classification and string processing techniques in Python.

---

## Code
```python
text = input("Enter a string: ")

letters = 0
digits = 0
special = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special characters:", special)
