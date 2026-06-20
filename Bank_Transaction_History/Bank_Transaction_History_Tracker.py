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






1. Deposit
2. Withdraw
3. View Transactions
4. Exit
Enter choice:  1
Enter deposit amount:  22000
