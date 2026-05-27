expenses = {}

n = int(input("How many expenses do you want to enter? "))

for i in range(n):
    item = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses[item] = amount

total = sum(expenses.values())

print("\nExpense Summary:")

for item, amount in expenses.items():
    print(f"{item} : ${amount}")

print(f"\nTotal Expense: ${total}")






How many expenses do you want to enter?  2
Enter expense name:  sid
Enter amount:  45
Enter expense name:  mon
Enter amount:  45

Expense Summary:
sid : $45.0
mon : $45.0

Total Expense: $90.0