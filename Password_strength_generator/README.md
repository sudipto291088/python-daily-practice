# Password Strength Checker in Python

## Overview
This program checks whether a password is strong or weak based on
basic password validation rules.

The program verifies:
- Minimum password length
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of numeric digits

---

## Program Description
The script:
- Accepts a password from the user
- Iterates through each character
- Checks for uppercase, lowercase, and numeric characters
- Validates the password strength
- Prints whether the password is strong or weak

---

## Code
```python
def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    if len(password) >= 8 and has_upper and has_lower and has_digit:
        return "Strong Password"
    else:
        return "Weak Password"


pwd = input("Enter your password: ")
print(check_password(pwd))
