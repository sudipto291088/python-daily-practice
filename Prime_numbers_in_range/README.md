# Prime Numbers in a Range – Python Program

## Overview
This program finds and prints all prime numbers within a given range.
It demonstrates loops, conditional logic, and nested iteration in Python.

---

## Code
```python
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print("Prime numbers are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
