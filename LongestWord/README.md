# Find the Longest Word in a Sentence – Python Program

## Overview
This program finds the longest word in a sentence.
It demonstrates string splitting, list processing, and the use of Python’s `max()` function with a custom key.

---

## Code
```python
sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = max(words, key=len)

print("Longest word:", longest_word)
print("Length:", len(longest_word))
