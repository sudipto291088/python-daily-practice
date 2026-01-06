## Two Sum

### Problem
Given an array of integers and a target value, return the indices of the two numbers such that they add up to the target.

### Approach
We iterate through the array once while storing previously seen numbers in a hash map.
For each number, we check if the complement (target - current number) already exists.
If it does, we return the indices.

### Time Complexity
O(n)

### Space Complexity
O(n)

### Key Concept
Hash map for constant-time lookup.

