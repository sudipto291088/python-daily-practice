
# Factorial Program in Python (Without Recursion)

## Overview
This program calculates the **factorial of a number without using recursion**.
Instead, it uses an **iterative approach with a `while` loop**, making the logic straightforward and easy to trace.

A key feature of this implementation is that it **prints each multiplication step**, helping beginners clearly understand how factorial computation progresses.

---

## Program Description
The script:
- Accepts a number from the user
- Computes the factorial using a loop (no recursion)
- Displays intermediate multiplication steps
- Handles the base case when the input is `0` or `1`

---

## Code
```python
def factworecursion(a):
    l = a
    if a > 1:
        while a > 1:
            a = a - 1
            print(l, '*', a, '=', l * a)
            l = l * a
    else:
        print(1)

m = int(input('Enter a number to find the factorial: '))
factworecursion(m)
