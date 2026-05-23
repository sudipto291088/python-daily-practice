# Armstrong Number Checker in Python

## Overview
This program checks whether a number is an Armstrong number.
An Armstrong number is a number whose sum of the cubes of its digits
is equal to the original number.

Example:
153 = 1³ + 5³ + 3³ = 153

---

## Code
```python
num = int(input("Enter a number: "))

temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp = temp // 10

if num == total:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
