# Count Vowels in a String – Python Program

## Overview
This program counts the number of **vowels present in a given string**.
It demonstrates basic string iteration, conditional logic, and function usage in Python.

---

## Program Description
The script:
- Accepts a string input from the user
- Iterates through each character of the string
- Checks whether the character is a vowel
- Counts the total number of vowels
- Prints the final count

---

## Code
```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in text:
        if ch in vowels:
            count += 1

    return count


s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))
