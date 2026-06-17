# Flight Booking System in Python

## Overview

This program simulates a simple flight booking system.

The application:
- Stores available flights
- Tracks seat availability
- Processes booking requests
- Updates remaining seats

The project demonstrates dictionaries, user input handling, conditional logic, and resource management.

---

## Code

```python
flights = {
    "AI101": 5,
    "BA202": 3,
    "UA303": 2
}

flight_no = input("Enter flight number: ").upper()

if flight_no in flights:

    seats = int(input("Enter number of seats to book: "))

    if seats <= flights[flight_no]:
        flights[flight_no] -= seats

        print("Booking Confirmed")
        print("Remaining Seats:", flights[flight_no])

    else:
        print("Not enough seats available")

else:
    print("Flight not found")
```

---

## How It Works

1. Flight numbers and available seats are stored in a dictionary
2. The user enters a flight number
3. The system verifies whether the flight exists
4. The user enters the number of seats to book
5. Seat availability is checked
6. If seats are available:
   - Booking is confirmed
   - Available seats are updated
7. Otherwise, an error message is displayed

---

## Example Run

### Input

```text
Enter flight number: AI101
Enter number of seats to book: 2
```

### Output

```text
Booking Confirmed
Remaining Seats: 3
```

---

## Concepts Covered

- Dictionaries
- Conditional statements
- User input handling
- Resource allocation
- Business rules

---

## Why This Program?

This project introduces:

- Reservation systems
- Inventory tracking
- Transaction processing
- Resource management

These concepts are commonly used in:

- Airline booking systems
- Hotel reservation systems
- Event ticketing platforms
- Travel applications

---

## Possible Improvements

- Add passenger details
- Store booking history
- Cancel bookings
- Generate tickets
- Save data to a file
- Support multiple flights and dates

---

## Author

Daily Python Practice  
Flight Booking System
