# Most Frequent Number (HashMap)

## Problem Statement
Given a list of integers provided by the user, determine which number appears
most frequently in the array.

---

## Input Description
- First, the user enters an integer representing the number of elements.
- Then, the user enters each element of the array one by one.

Example input:

Enter a range for the array: 6
1
2
2
3
3
3


---

## Output Description
The program prints the number that appears most frequently in the array.

Example output:

the most frequent number is 3


---

## Approach
- Use a hash map (dictionary) to count the frequency of each number.
- Traverse the array once and update counts.
- Track the maximum frequency seen so far.
- Update the result whenever a higher frequency is found.

This ensures the solution runs efficiently in a single pass.

---

## Time Complexity
- **O(n)**  
  The array is traversed once.

## Space Complexity
- **O(n)**  
  Extra space is used to store frequency counts in a hash map.

---

## Key Concepts Used
- Hash Map (Dictionary)
- Array Traversal
- Time and Space Complexity
- Frequency Counting

---
