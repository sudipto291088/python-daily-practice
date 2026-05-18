# Anagram Checker in Python

## Overview
This program checks whether two strings are anagrams of each other.
Two strings are considered anagrams if they contain the same characters
in a different order.

Examples:
- listen → silent
- race → care

---

## Code
```python
str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

if sorted(str1) == sorted(str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
