# Word Frequency Counter in Python

## Overview
This program counts the frequency of each word in a sentence.
It demonstrates the use of dictionaries, loops, conditionals,
and string manipulation in Python.

---

## Program Description
The script:
- Accepts a sentence from the user
- Converts the sentence to lowercase
- Splits the sentence into words
- Counts how many times each word appears
- Displays the word frequencies

---

## Code
```python
def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


s = input("Enter a sentence: ")

result = word_frequency(s)

for word, count in result.items():
    print(f"{word} : {count}")
