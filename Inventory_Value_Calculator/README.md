# Inventory Value Calculator in Python

## Overview

This program calculates the total inventory value of products in stock.

Each product contains:
- Product name
- Unit price
- Available quantity

The application computes the stock value for every product and the overall inventory value.

---

## Code

```python
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
```

---

## How It Works

1. Inventory records are stored as a list of dictionaries.
2. Each record contains a product, price, and quantity.
3. The program loops through every product.
4. Individual stock value is calculated using:

   Stock Value = Price × Quantity

5. The values are accumulated to calculate the total inventory value.
6. A detailed inventory report is displayed.

---

## Example Output

```text
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
```

---

## Concepts Covered

- Lists
- Dictionaries
- Nested data structures
- Loops
- Arithmetic operations
- Data aggregation
- Business reporting

---

## Why This Program?

This project demonstrates how inventory information can be processed to generate business insights.

These techniques are commonly used in:

- Warehouse Management Systems
- Retail Analytics
- ERP Software
- Inventory Dashboards
- Supply Chain Management

---

## Possible Improvements

- Read inventory data from a CSV file
- Sort products by inventory value
- Identify low-stock products
- Add restocking functionality
- Export reports to Excel

---

## Author

Daily Python Practice

Inventory Value Calculator
