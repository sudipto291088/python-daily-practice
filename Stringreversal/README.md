# String Reversal in Python Using Slicing

## Overview
This program demonstrates how to **reverse a string in Python** using
**string slicing**. It shows a clean and Pythonic way to reverse text
without using loops or built-in reverse functions.

---

## Program Description
The script:
- Defines a function to reverse a string
- Takes user input from the console
- Reverses the input string using slicing
- Returns the reversed string

---

## Code
```python
def rev(s):
    return s[::-1]

a = input("Enter a string..")
rev(a)



Enter a string..
python


nohtyp
