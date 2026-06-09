# Weather Data Analyzer in Python

## Overview

This program analyzes a week's temperature data and generates basic weather statistics.

The application:
- Calculates average temperature
- Finds the highest temperature
- Finds the lowest temperature
- Counts days above average temperature

The project demonstrates loops, lists, aggregation, and basic data analysis techniques.

---

## Code

```python
temperatures = [72, 68, 75, 80, 77, 69, 85]

average_temp = sum(temperatures) / len(temperatures)

highest_temp = max(temperatures)
lowest_temp = min(temperatures)

days_above_average = 0

for temp in temperatures:
    if temp > average_temp:
        days_above_average += 1

print("Average Temperature:", round(average_temp, 2))
print("Highest Temperature:", highest_temp)
print("Lowest Temperature:", lowest_temp)
print("Days Above Average:", days_above_average)
```

---

## How It Works

1. Temperature values are stored in a list
2. The average temperature is calculated
3. The highest and lowest temperatures are identified
4. A loop counts temperatures above the average
5. Summary statistics are displayed

---

## Example Output

```text
Average Temperature: 75.14
Highest Temperature: 85
Lowest Temperature: 68
Days Above Average: 3
```

---

## Concepts Covered

- Lists
- Loops
- Conditional statements
- sum()
- max()
- min()
- Data analysis

---

## Why This Program?

This project introduces:

- Descriptive statistics
- Data summarization
- Trend analysis
- Analytical reporting

These concepts are commonly used in:

- Weather forecasting
- Business analytics
- Data Science
- Monitoring systems

---

## Possible Improvements

- Accept temperature data from user input
- Calculate median temperature
- Plot temperature trends
- Store readings in a CSV file
- Generate weekly weather reports

---

## Author

Daily Python Practice  
Weather Data Analyzer
