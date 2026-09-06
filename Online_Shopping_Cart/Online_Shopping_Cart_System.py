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