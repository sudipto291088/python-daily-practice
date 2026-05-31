inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Monitor": 8
}

print("Current Inventory:\n")

for item, qty in inventory.items():
    print(f"{item}: {qty}")

product = input("\nEnter product name: ")

if product in inventory:
    sold = int(input("Enter quantity sold: "))

    if sold <= inventory[product]:
        inventory[product] -= sold
        print(f"Updated stock for {product}: {inventory[product]}")
    else:
        print("Insufficient stock")
else:
    print("Product not found")




Current Inventory:

Laptop: 10
Mouse: 25
Keyboard: 15
Monitor: 8

Enter product name:  chess
Product not found