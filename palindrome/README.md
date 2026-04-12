# Palindrome Checker in Python

## Overview
This program checks whether a given string is a **palindrome**.
A palindrome is a word, phrase, or sequence that reads the same
forward and backward.

Examples include: `madam`, `racecar`, and `level`.

---

## Program Description
The script:
- Takes a string input from the user
- Converts the text to lowercase for consistency
- Removes spaces to allow phrase comparison
- Compares the string with its reversed version
- Prints whether the string is a palindrome

---

## Code
```python
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


s = input("Enter a string: ")

if is_palindrome(s):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
