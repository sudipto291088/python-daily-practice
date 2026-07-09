# Product Price Ranking System in Python

## Overview

This program ranks products based on their prices in descending order.

The application:
- Stores product information
- Sorts products by price
- Displays products from the most expensive to the least expensive

The project demonstrates sorting techniques, lists of dictionaries, lambda functions, and ranking logic.

---

## Code

```python
products = [
    {"Name": "Laptop", "Price": 900},
    {"Name": "Mouse", "Price": 25},
    {"Name": "Keyboard", "Price": 60},
    {"Name": "Monitor", "Price": 300},
    {"Name": "Headphones", "Price": 120}
]

sorted_products = sorted(products, key=lambda product: product["Price"], reverse=True)

print("Product Price Ranking")
print("-" * 35)

rank = 1

for product in sorted_products:
    print(f"{rank}. {product['Name']} - ${product['Price']}")
    rank += 1
```

---

## How It Works

1. Product records are stored in a list of dictionaries.
2. The built-in `sorted()` function sorts the products.
3. A `lambda` function specifies that sorting should be based on the `Price` field.
4. `reverse=True` sorts the products from highest to lowest price.
5. A ranking number is assigned and displayed.

---

## Example Output

```text
Product Price Ranking
-----------------------------------

1. Laptop - $900
2. Monitor - $300
3. Headphones - $120
4. Keyboard - $60
5. Mouse - $25
```

---

## Concepts Covered

- Lists
- Dictionaries
- `sorted()`
- Lambda functions
- Ranking algorithms
- Data presentation

---

## Why This Program?

This project introduces:

- Custom sorting
- Ranking systems
- Record processing
- Business analytics

These concepts are commonly used in:

- E-commerce platforms
- Product catalogs
- Recommendation systems
- Business dashboards
- Data analytics applications

---

## Possible Improvements

- Sort by product name
- Sort in ascending order
- Filter products above a given price
- Read product data from a CSV file
- Display the top N most expensive products

---

## Author

Daily Python Practice

Product Price Ranking System
