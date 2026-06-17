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