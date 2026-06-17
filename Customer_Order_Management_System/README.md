# Customer Order Management System in Python

## Overview

This program simulates a simple customer order management system.

The application:
- Stores customer orders
- Calculates order totals
- Counts items per order
- Generates an order summary report

The project demonstrates dictionaries, lists, loops, and business reporting logic.

---

## Code

```python
orders = {
    "Order001": [120, 80, 50],
    "Order002": [200, 150],
    "Order003": [90, 60, 40, 30]
}

for order_id, items in orders.items():
    total = sum(items)

    print(f"{order_id}")
    print(f"Items: {len(items)}")
    print(f"Total Amount: ${total}")
    print("-" * 20)
```

---

## How It Works

1. Orders are stored in a dictionary
2. Each order contains a list of item prices
3. The program loops through all orders
4. The total amount is calculated using `sum()`
5. The number of items is calculated using `len()`
6. A formatted order report is displayed

---

## Example Output

```text
Order001
Items: 3
Total Amount: $250
--------------------

Order002
Items: 2
Total Amount: $350
--------------------

Order003
Items: 4
Total Amount: $220
--------------------
```

---

## Concepts Covered

- Dictionaries
- Lists
- Loops
- sum()
- len()
- Business reporting

---

## Why This Program?

This project introduces:

- Order processing
- Sales calculations
- Transaction reporting
- Data aggregation

These concepts are commonly used in:

- E-commerce platforms
- Billing systems
- Retail applications
- Inventory systems

---

## Possible Improvements

- Add customer names
- Calculate taxes
- Generate invoices
- Store order dates
- Export reports to CSV
- Track order status

---

## Author

Daily Python Practice  
Customer Order Management System
