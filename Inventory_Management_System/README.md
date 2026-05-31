# Inventory Management System in Python

## Overview

This program simulates a basic inventory management system.

Users can:
- View available products
- Select a product
- Record product sales
- Update inventory quantities

The project demonstrates dictionaries, loops, conditional logic, and inventory tracking.

---

## Code

```python
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
```

---

## How It Works

1. Products and quantities are stored in a dictionary
2. Available inventory is displayed
3. The user selects a product
4. The quantity sold is entered
5. The inventory is updated
6. The new stock level is displayed

---

## Example Run

### Input

```text
Enter product name: Laptop
Enter quantity sold: 3
```

### Output

```text
Updated stock for Laptop: 7
```

---

## Concepts Covered

- Dictionaries
- Loops
- Conditional statements
- User input handling
- Inventory management logic

---

## Why This Program?

This project introduces real-world concepts such as:

- Stock tracking
- Inventory updates
- Product management
- Business operations

These concepts are commonly used in:

- Retail systems
- Warehouse software
- E-commerce platforms
- Inventory dashboards

---

## Possible Improvements

- Add new products
- Remove products
- Restock inventory
- Store prices
- Calculate inventory value
- Save inventory to a file

---

## Author

Daily Python Practice  
Inventory Management System
