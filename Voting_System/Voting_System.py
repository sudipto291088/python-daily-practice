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





Vote Counts:
Alice: 3
Bob: 2
John: 1

Winner: Alice