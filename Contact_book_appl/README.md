# Contact Book Application in Python

## Overview

This program simulates a simple Contact Book application.

Users can:
- Add contacts
- View all contacts
- Search for a contact
- Exit the application

The project demonstrates dictionaries, loops, user input handling, and basic data management.

---

## Code

```python
contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        for name, phone in contacts.items():
            print(f"{name} : {phone}")

    elif choice == "3":
        name = input("Enter name to search: ")

        if name in contacts:
            print(f"{name} : {contacts[name]}")
        else:
            print("Contact not found")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
```

---

## How It Works

1. Contacts are stored in a dictionary
2. The user chooses an operation from the menu
3. New contacts can be added
4. Existing contacts can be viewed
5. Specific contacts can be searched
6. The program continues until the user exits

---

## Example Run

### Input

```text
1
John
555-1234

1
Alice
555-5678

2
```

### Output

```text
John : 555-1234
Alice : 555-5678
```

---

## Concepts Covered

- Dictionaries
- While loops
- Conditional statements
- User input handling
- Data storage and retrieval

---

## Why This Program?

This project introduces:

- Contact management systems
- CRUD operations
- Interactive menu-driven applications
- Real-world data organization

These concepts are commonly used in:
- Address books
- Customer databases
- Employee directories
- Business applications

---

## Possible Improvements

- Delete contacts
- Update contact information
- Save contacts to a file
- Import/export contacts
- Validate phone numbers

---

## Author

Daily Python Practice  
Contact Book Application
