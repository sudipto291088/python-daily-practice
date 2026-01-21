# Python Variable Scope Example (Global, Local, and Nested Functions)

## Overview
This program demonstrates how **variable scope** works in Python by using:
- A global variable
- A variable inside an outer function
- A variable inside an inner (nested) function

It clearly shows how Python accesses variables at different levels of scope.

---

## Program Description
The script:
- Declares a global variable
- Defines an outer function with its own local variable
- Defines an inner function nested inside the outer function
- Prints variables from different scopes to illustrate accessibility

---

## Code
```python
global_var = 10

def outer_func():
    outer_var = 20
    def inner_func():
        inner_var = 30
        print(inner_var)
    print(outer_var)
    inner_func()

print(global_var)
outer_func()
