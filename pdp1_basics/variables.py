"""
Variables – Python Basics
Covered:
- assignment
- data types
- arithmetic operators
- strings and f-strings
"""

# Basic variables
age = 36
height = 5.5
name = "Sid"
is_student = True

print(age, height, name, is_student)

# Data types
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

# Arithmetic operators
x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)

# Strings
first_name = "Sudipto"
last_name = "Bhadra"

full_name = first_name + " " + last_name
print(full_name)
print(full_name.upper())
print(full_name.lower())
print(len(full_name))

# String formatting
city = "SilverSpring"
profession = "IT"
yoe = 10
year = 2025

print(
    f"My name is Sid. I live in {city}. "
    f"I work as {profession}. "
    f"I have {yoe} years of experience as of {year}."
)