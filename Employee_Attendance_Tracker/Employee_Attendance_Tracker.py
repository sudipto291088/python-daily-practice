attendance = {
    "John": "Present",
    "Alice": "Absent",
    "Bob": "Present",
    "David": "Present",
    "Emma": "Absent"
}

present_count = 0
absent_count = 0

for employee, status in attendance.items():
    if status == "Present":
        present_count += 1
    else:
        absent_count += 1

attendance_percentage = (present_count / len(attendance)) * 100

print("Present Employees:", present_count)
print("Absent Employees:", absent_count)
print("Attendance Percentage:", round(attendance_percentage, 2), "%")





Present Employees: 3
Absent Employees: 2
Attendance Percentage: 60.0 %