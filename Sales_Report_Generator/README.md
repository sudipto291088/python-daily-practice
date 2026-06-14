# Sales Report Generator in Python

## Overview

This program generates a simple sales report using monthly sales data.

The application:
- Calculates total sales
- Calculates average sales
- Identifies the best-performing month
- Identifies the lowest-performing month

The project demonstrates dictionaries, aggregation functions, and business reporting techniques.

---

## Code

```python
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
```

---

## How It Works

1. Monthly sales figures are stored in a dictionary
2. Total sales are calculated using `sum()`
3. Average sales are computed
4. `max()` identifies the best-performing month
5. `min()` identifies the lowest-performing month
6. A summary report is displayed

---

## Example Output

```text
Sales Report
--------------------

Total Sales: 72000
Average Sales: 14400.0

Best Month: April - 18000
Worst Month: March - 11000
```

---

## Concepts Covered

- Dictionaries
- sum()
- max()
- min()
- Business analytics
- Reporting

---

## Why This Program?

This project introduces:

- Sales analytics
- Business reporting
- Performance tracking
- Summary statistics

These concepts are commonly used in:

- BI dashboards
- Retail analytics
- Financial reporting
- Data Science projects

---

## Possible Improvements

- Accept monthly sales from user input
- Generate quarterly reports
- Display sales trends
- Export results to CSV
- Create visual charts using Matplotlib

---

## Author

Daily Python Practice  
Sales Report Generator
