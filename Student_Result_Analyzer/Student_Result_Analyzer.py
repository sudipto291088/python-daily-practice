students = {
    "John": 78,
    "Alice": 92,
    "Bob": 65,
    "David": 55,
    "Emma": 88
}

total_marks = sum(students.values())
average_marks = total_marks / len(students)

topper = max(students, key=students.get)

passed = 0
failed = 0

for marks in students.values():
    if marks >= 60:
        passed += 1
    else:
        failed += 1

print("Average Marks:", round(average_marks, 2))
print("Topper:", topper)
print("Passed Students:", passed)
print("Failed Students:", failed)






Average Marks: 75.6
Topper: Alice
Passed Students: 4
Failed Students: 1