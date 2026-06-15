employees = {
    "John": 10,
    "Alice": 15,
    "Bob": 8
}

name = input("Enter employee name: ")

if name in employees:
    requested_days = int(input("Enter leave days requested: "))

    if requested_days <= employees[name]:
        employees[name] -= requested_days
        print("Leave Approved")
        print("Remaining Leave Balance:", employees[name])
    else:
        print("Insufficient Leave Balance")
else:
    print("Employee Not Found")



Enter employee name:  John
Enter leave days requested:  5
Leave Approved
Remaining Leave Balance: 5
