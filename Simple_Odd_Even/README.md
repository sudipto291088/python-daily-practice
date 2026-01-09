# Odd and Even Number Separation

## Problem Statement
Given a number `n` entered by the user, generate numbers from `0` to `n-1` and
separate them into **odd** and **even** lists.

---

## Input Description
- The user provides a single integer representing the range of numbers.

Example input:

Enter a range for the array: 6


---

## Output Description
- The program prints two lists:
  - one containing odd numbers
  - one containing even numbers

Example output:
[1, 3, 5] [0, 2, 4]


---

## Approach
- Initialize two empty lists: one for odd numbers and one for even numbers.
- Loop through numbers from `0` to `n-1`.
- Use the modulo operator (`%`) to check:
  - if a number is divisible by 2 → even
  - otherwise → odd
- Append each number to the appropriate list.

---

## Implementation

```python
odd = []
even = []

a = int(input('Enter a range for the array'))

for i in range(a):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(odd, even)
