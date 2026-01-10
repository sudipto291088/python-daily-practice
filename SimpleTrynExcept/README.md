# Python Exception Handling – try / except

## Overview
This program demonstrates basic exception handling in Python using a `try–except` block.
It safely handles runtime errors that may occur during user input or division operations.

## Program Description
The script:
- Takes a number as user input
- Converts the input into an integer
- Divides a fixed value (`a = 10`) by the user input
- Catches and prints any exception instead of crashing

## Code
```python
try:
    a = 10
    b = int(input('Enter a number: '))
    print(a / b)
except Exception as err:
    print(f"root cause of exception is: {err}")

Enter a number: 2
5.0

Enter a number: 0
root cause of exception is: division by zero

