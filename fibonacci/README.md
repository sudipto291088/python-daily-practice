# Fibonacci Series Generator in Python

## Overview
This program generates the Fibonacci sequence up to a specified number of terms.
The Fibonacci series is a sequence where each number is the sum of the two previous numbers.

---

## Code
```python
n = int(input("Enter the number of terms: "))

a, b = 0, 1

print("Fibonacci Series:")

for i in range(n):
    print(a)
    a, b = b, a + b
