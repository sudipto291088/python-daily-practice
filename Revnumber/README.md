# Reverse a Number in Python Using String Conversion

## Overview
This program demonstrates how to **reverse a number in Python** by first
converting the number into a string and then using **string slicing**.
It shows a simple and effective way to manipulate numeric data using strings.

---

## Program Description
The script:
- Defines a function to reverse a number
- Converts the number to a string
- Reverses the string using slicing
- Returns the reversed value

---

## Code
```python
def revnumber(x):
    return str(x)[::-1]

revnumber(2348927)


'7298432'
