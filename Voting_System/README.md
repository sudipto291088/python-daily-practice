# Voting System and Winner Finder in Python

## Overview

This program simulates a simple voting system.

It:
- Counts votes for each candidate
- Stores vote totals in a dictionary
- Determines the winner based on the highest vote count

The project demonstrates dictionaries, loops, counting logic, and data analysis techniques.

---

## Code

```python
votes = ["Alice", "Bob", "Alice", "John", "Bob", "Alice"]

results = {}

for candidate in votes:
    if candidate in results:
        results[candidate] += 1
    else:
        results[candidate] = 1

winner = max(results, key=results.get)

print("Vote Counts:")
for candidate, count in results.items():
    print(f"{candidate}: {count}")

print(f"\nWinner: {winner}")
```

---

## How It Works

1. A list of votes is created
2. A dictionary stores vote counts
3. The program loops through all votes
4. Each candidate's vote total is updated
5. The candidate with the highest vote count is identified
6. The results and winner are displayed

---

## Example Output

```text
Vote Counts:
Alice: 3
Bob: 2
John: 1

Winner: Alice
```

---

## Concepts Covered

- Dictionaries
- Loops
- Frequency counting
- max()
- Data aggregation

---

## Why This Program?

This project introduces:

- Election result processing
- Frequency analysis
- Data summarization
- Winner determination logic

These concepts are commonly used in:

- Voting systems
- Surveys
- Polling applications
- Analytics dashboards

---

## Possible Improvements

- Accept votes from user input
- Handle ties
- Display vote percentages
- Store results in a file
- Support multiple elections

---

## Author

Daily Python Practice  
Voting System and Winner Finder
