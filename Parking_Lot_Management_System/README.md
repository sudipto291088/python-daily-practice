# Parking Lot Management System in Python

## Overview

This program simulates a basic parking lot management system.

The application:
- Tracks parking capacity
- Calculates available parking slots
- Processes incoming vehicles
- Updates occupancy information

The project demonstrates arithmetic operations, conditional logic, and resource allocation concepts.

---

## Code

```python
parking_capacity = 10
occupied = 6

print("Total Parking Slots:", parking_capacity)
print("Occupied Slots:", occupied)

available = parking_capacity - occupied

print("Available Slots:", available)

cars_entering = int(input("Enter number of incoming cars: "))

if cars_entering <= available:
    occupied += cars_entering
    print("Cars Parked Successfully")
    print("Updated Occupied Slots:", occupied)
else:
    print("Parking Full! Not enough space.")
```

---

## How It Works

1. Total parking capacity is defined
2. Current occupied slots are tracked
3. Available slots are calculated
4. The user enters the number of incoming cars
5. The system checks space availability
6. Occupancy is updated if sufficient space exists

---

## Example Run

### Input

```text
Enter number of incoming cars: 3
```

### Output

```text
Total Parking Slots: 10
Occupied Slots: 6
Available Slots: 4

Cars Parked Successfully
Updated Occupied Slots: 9
```

---

## Concepts Covered

- Variables
- Arithmetic operations
- Conditional statements
- User input handling
- Resource management

---

## Why This Program?

This project introduces:

- Capacity planning
- Availability tracking
- Resource allocation
- Operational management

These concepts are commonly used in:

- Parking systems
- Hotel booking systems
- Flight reservations
- Inventory management

---

## Possible Improvements

- Track vehicle numbers
- Support vehicle exits
- Store parking history
- Generate occupancy reports
- Save data to a file

---

## Author

Daily Python Practice  
Parking Lot Management System
