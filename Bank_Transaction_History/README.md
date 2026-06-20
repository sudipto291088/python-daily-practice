# Bank Transaction History Tracker in Python

## Overview

This program simulates a simple banking transaction tracker.

Users can:
- Deposit money
- Withdraw money
- View transaction history
- Check current balance

The project demonstrates lists, loops, conditional logic, and transaction management.

---

## Code

```python
balance = 1000
transactions = []

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. View Transactions")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        transactions.append(f"Deposited ${amount}")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            transactions.append(f"Withdrew ${amount}")
        else:
            print("Insufficient Funds")

    elif choice == "3":
        print("\nTransaction History:")
        for transaction in transactions:
            print(transaction)

        print(f"\nCurrent Balance: ${balance}")

    elif choice == "4":
        break

    else:
        print("Invalid Choice")
```

---

## How It Works

1. An initial account balance is created
2. Transactions are stored in a list
3. Users can deposit or withdraw funds
4. Each transaction is recorded
5. Transaction history can be viewed at any time
6. Current balance is displayed along with transaction history

---

## Example Run

### Output

```text
Deposited $500
Withdrew $200

Transaction History:
Deposited $500
Withdrew $200

Current Balance: $1300
```

---

## Concepts Covered

- Lists
- While loops
- Conditional statements
- User input handling
- Transaction logging

---

## Why This Program?

This project introduces:

- Banking workflows
- Audit trails
- Transaction history management
- Stateful applications

These concepts are commonly used in:

- Banking software
- Financial applications
- Accounting systems
- Payment platforms

---

## Possible Improvements

- Add timestamps
- Transfer funds
- Multiple accounts
- Export transaction history
- PIN authentication
- Monthly statements

---

## Author

Daily Python Practice  
Bank Transaction History Tracker
