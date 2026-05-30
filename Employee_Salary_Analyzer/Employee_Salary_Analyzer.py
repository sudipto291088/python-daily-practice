employees = {
    "John": 55000,
    "Alice": 72000,
    "Bob": 48000,
    "David": 81000
}

highest_paid = max(employees, key=employees.get)
lowest_paid = min(employees, key=employees.get)

average_salary = sum(employees.values()) / len(employees)

print("Highest Paid Employee:", highest_paid)
print("Salary:", employees[highest_paid])

print("\nLowest Paid Employee:", lowest_paid)
print("Salary:", employees[lowest_paid])

print("\nAverage Salary:", average_salary)





Highest Paid Employee: David
Salary: 81000

Lowest Paid Employee: Bob
Salary: 48000

Average Salary: 64000.0


