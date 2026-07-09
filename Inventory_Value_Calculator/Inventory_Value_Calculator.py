inventory = [
    {"Product": "Laptop", "Price": 800, "Quantity": 5},
    {"Product": "Mouse", "Price": 20, "Quantity": 30},
    {"Product": "Keyboard", "Price": 50, "Quantity": 15},
    {"Product": "Monitor", "Price": 250, "Quantity": 8}
]

grand_total = 0

print("Inventory Report")
print("-" * 40)

for item in inventory:
    value = item["Price"] * item["Quantity"]
    grand_total += value

    print(f"{item['Product']}")
    print(f"Price      : ${item['Price']}")
    print(f"Quantity   : {item['Quantity']}")
    print(f"Stock Value: ${value}")
    print("-" * 40)

print("Total Inventory Value:", grand_total)





Inventory Report
----------------------------------------
Laptop
Price      : $800
Quantity   : 5
Stock Value: $4000
----------------------------------------
Mouse
Price      : $20
Quantity   : 30
Stock Value: $600
----------------------------------------
Keyboard
Price      : $50
Quantity   : 15
Stock Value: $750
----------------------------------------
Monitor
Price      : $250
Quantity   : 8
Stock Value: $2000
----------------------------------------
Total Inventory Value: 7350