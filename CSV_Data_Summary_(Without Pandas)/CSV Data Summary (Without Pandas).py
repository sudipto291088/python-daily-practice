employees = [
    {"Name": "John", "Age": 28, "Salary": 55000},
    {"Name": "Alice", "Age": 35, "Salary": 72000},
    {"Name": "Bob", "Age": 30, "Salary": 48000},
    {"Name": "David", "Age": 42, "Salary": 81000}
]

total_salary = 0
oldest_employee = employees[0]

for employee in employees:
    total_salary += employee["Salary"]

    if employee["Age"] > oldest_employee["Age"]:
        oldest_employee = employee

average_salary = total_salary / len(employees)

print("Employee Summary")
print("-" * 30)

print("Average Salary:", average_salary)
print("Oldest Employee:", oldest_employee["Name"])
print("Highest Age:", oldest_employee["Age"])



Employee Summary
------------------------------
Average Salary: 64000.0
Oldest Employee: David
Highest Age: 42