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




1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice:  1
Current Balance: $1000

1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice:  2
Enter deposit amount:  700
Updated Balance: $1700.0