# Most Frequent Number (HashMap – Function Based)

## Problem Statement
Given a list of integers, determine which number appears most frequently.

This solution is written using a **function-based approach**, making it reusable,
testable, and suitable for interview scenarios.

---

## Approach
- Traverse the list once.
- Use a hash map (dictionary) to count the frequency of each number.
- Track the maximum frequency encountered so far.
- Update the result whenever a higher frequency is found.

This approach ensures optimal performance.

---

## Implementation

```python
def most_frequent_number(arr):
    count = {}
    max_count = 0
    most_frequent = None

    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

        if count[num] > max_count:
            max_count = count[num]
            most_frequent = num

    return most_frequent


arr = [1, 2, 2, 3, 3, 3]
print(most_frequent_number(arr))

3
