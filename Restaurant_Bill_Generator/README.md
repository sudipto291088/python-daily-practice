# Restaurant Bill Generator in Python

## Overview

This program simulates a simple restaurant billing system.

The application:
- Stores menu items and prices
- Processes customer orders
- Calculates subtotal
- Calculates tax
- Generates a final bill

The project demonstrates dictionaries, loops, arithmetic operations, and report generation.

---

## Code

```python
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
```

---

## How It Works

1. Menu items and prices are stored in a dictionary
2. Customer orders are stored in a list
3. The program loops through ordered items
4. Prices are added to calculate the subtotal
5. Tax is calculated at 10%
6. The final bill is generated

---

## Example Output

```text
Customer Bill
--------------------
Burger: $8
Pizza: $12
Coke: $3
--------------------
Subtotal: 23
Tax (10%): 2.3
Grand Total: 25.3
```

---

## Concepts Covered

- Dictionaries
- Lists
- Loops
- Arithmetic operations
- Bill generation
- Reporting

---

## Why This Program?

This project introduces:

- Billing systems
- Order processing
- Financial calculations
- Report generation

These concepts are commonly used in:

- Restaurants
- E-commerce platforms
- Retail stores
- POS (Point of Sale) systems

---

## Possible Improvements

- Accept orders from user input
- Support item quantities
- Add discounts
- Generate receipts
- Save orders to a file

---

## Author

Daily Python Practice  
Restaurant Bill Generator
