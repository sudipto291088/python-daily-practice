sales = {
    "January": 12000,
    "February": 15000,
    "March": 11000,
    "April": 18000,
    "May": 16000
}

total_sales = sum(sales.values())
average_sales = total_sales / len(sales)

best_month = max(sales, key=sales.get)
worst_month = min(sales, key=sales.get)

print("Sales Report")
print("-" * 20)

print("Total Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))
print("Best Month:", best_month, "-", sales[best_month])
print("Worst Month:", worst_month, "-", sales[worst_month])





Sales Report
--------------------
Total Sales: 72000
Average Sales: 14400.0
Best Month: April - 18000
Worst Month: March - 11000