# Sort Words in Alphabetical Order – Python Program

## Overview
This program sorts the words in a sentence in alphabetical order.
It demonstrates string splitting, list sorting, and iteration in Python.

---

## Code
```python
sentence = input("Enter a sentence: ")

words = sentence.split()

words.sort()

print("Words in alphabetical order:")

for word in words:
    print(word)
