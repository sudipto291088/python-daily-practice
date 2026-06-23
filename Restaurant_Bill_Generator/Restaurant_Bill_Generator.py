menu = {
    "Burger": 8,
    "Pizza": 12,
    "Pasta": 10,
    "Coke": 3
}

order = ["Burger", "Pizza", "Coke"]

total_bill = 0

print("Customer Bill")
print("-" * 20)

for item in order:
    print(f"{item}: ${menu[item]}")
    total_bill += menu[item]

tax = total_bill * 0.10
grand_total = total_bill + tax

print("-" * 20)
print("Subtotal:", total_bill)
print("Tax (10%):", round(tax, 2))
print("Grand Total:", round(grand_total, 2))




Customer Bill
--------------------
Burger: $8
Pizza: $12
Coke: $3
--------------------
Subtotal: 23
Tax (10%): 2.3
Grand Total: 25.3