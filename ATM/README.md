# ATM Simulation System in Python

## Overview

This program simulates a basic ATM system.

Users can:
- Check account balance
- Deposit money
- Withdraw money
- Exit the application

The project demonstrates loops, conditional statements, user input handling, and basic financial transaction logic.

---

## Code

```python
balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Current Balance: ${balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print(f"Updated Balance: ${balance}")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print(f"Updated Balance: ${balance}")
        else:
            print("Insufficient Funds")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid Choice")
```

---

## How It Works

1. The account starts with an initial balance
2. A menu is displayed continuously using a loop
3. Users select an operation
4. The balance is updated based on deposits or withdrawals
5. The program exits when the user chooses Exit

---

## Example Run

```text
1. Check Balance
2. Deposit
3. Withdraw
4. Exit

Enter your choice: 2
Enter deposit amount: 500

Updated Balance: $1500
```

---

## Concepts Covered

- While loops
- Conditional statements
- User input handling
- Financial calculations
- Menu-driven programs

---

## Why This Program?

This project introduces:

- Banking transaction logic
- State management
- Interactive console applications
- Real-world business workflows

---

## Possible Improvements

- PIN authentication
- Transaction history
- Multiple accounts
- Transfer funds
- Save data to a file
- Interest calculation

---

## Author

Daily Python Practice  
ATM Simulation System
