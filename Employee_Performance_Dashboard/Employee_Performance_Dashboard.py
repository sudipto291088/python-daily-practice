employees = {
    "John": 85,
    "Alice": 92,
    "Bob": 74,
    "David": 88,
    "Emma": 95
}

average_score = sum(employees.values()) / len(employees)

top_performer = max(employees, key=employees.get)

print("Employee Performance Report")
print("-" * 30)

for employee, score in employees.items():
    status = "Above Average" if score > average_score else "Below Average"

    print(f"{employee}: {score} ({status})")

print("\nAverage Score:", round(average_score, 2))
print("Top Performer:", top_performer)



Employee Performance Report
------------------------------
John: 85 (Below Average)
Alice: 92 (Above Average)
Bob: 74 (Below Average)
David: 88 (Above Average)
Emma: 95 (Above Average)

Average Score: 86.8
Top Performer: Emma