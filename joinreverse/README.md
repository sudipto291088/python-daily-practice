# String Reversal in Python Using reversed() and join()

## Overview
This program demonstrates how to **reverse a string in Python** using the
built-in `reversed()` function combined with the `join()` method.
It highlights an alternative approach to string reversal without slicing.

---

## Program Description
The script:
- Defines a string value
- Uses the `reversed()` function to reverse the string character by character
- Combines the reversed characters into a new string using `join()`
- Stores the reversed string in a variable

---

## Code
```python
a = "learning python is important"

s = "".join(reversed(a))

s



tnatropmi si nohtyp gninrael
