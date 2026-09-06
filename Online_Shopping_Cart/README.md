# Online Shopping Cart System in Python

## Overview

This project implements a simple online shopping cart system using Python.

The program stores product prices, allows products to be added to a shopping cart, tracks quantities, and calculates the final bill.

---

## Features

- Store products and prices
- Add products to a shopping cart
- Track product quantities
- Calculate individual item costs
- Calculate the total shopping bill
- Handle unavailable products

---

## Code

```python
products = {
    "Laptop": 900,
    "Mouse": 25,
    "Keyboard": 60,
    "Headphones": 120
}

cart = {}

def add_to_cart(product, quantity):
    if product in products:
        cart[product] = cart.get(product, 0) + quantity
        print(f"{product} added to cart.")
    else:
        print("Product not found.")


def calculate_total():
    total = 0

    for product, quantity in cart.items():
        total += products[product] * quantity

    return total


add_to_cart("Laptop", 1)
add_to_cart("Mouse", 2)
add_to_cart("Headphones", 1)

print("\nShopping Cart")
print("-" * 35)

for product, quantity in cart.items():
    cost = products[product] * quantity
    print(f"{product} x {quantity} = ${cost}")

print("-" * 35)
print("Total Bill: $", calculate_total())
```

---

## How It Works

1. Product names and prices are stored in a dictionary.
2. Another dictionary stores products added to the cart.
3. `add_to_cart()` checks whether a product exists and updates its quantity.
4. `cart.get()` retrieves the current quantity or returns `0` if the product has not been added before.
5. `calculate_total()` loops through the cart and calculates the total cost.
6. The final shopping cart and bill are displayed.

---

## Example Output

```text
Laptop added to cart.
Mouse added to cart.
Headphones added to cart.

Shopping Cart
-----------------------------------
Laptop x 1 = $900
Mouse x 2 = $50
Headphones x 1 = $120
-----------------------------------
Total Bill: $ 1070
```

---

## Concepts Covered

- Functions
- Dictionaries
- Loops
- Conditional statements
- `.get()` method
- Function parameters
- Return values
- Data aggregation

---

## Why This Program?

This project demonstrates the basic logic behind a shopping cart used in e-commerce applications.

Similar concepts are used in:

- E-commerce websites
- Retail applications
- Point-of-sale systems
- Order management systems
- Checkout systems

---

## Possible Improvements

- Accept products from user input
- Remove products from the cart
- Apply discounts
- Calculate sales tax
- Validate quantities
- Save orders to a file
- Generate receipts

---

## Author

Daily Python Practice

Online Shopping Cart System
