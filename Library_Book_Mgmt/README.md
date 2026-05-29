# Library Book Search System in Python

## Overview
This program simulates a simple library book search system.
Users can search for a book by title, and the program checks whether the book exists in the library collection.

The project demonstrates the use of:
- Lists
- Dictionaries
- Loops
- String matching
- Search algorithms

---

## Code

```python
books = [
    {"id": 1, "title": "Python Basics"},
    {"id": 2, "title": "Data Science"},
    {"id": 3, "title": "Machine Learning"}
]

search = input("Enter book title to search: ").lower()

found = False

for book in books:
    if search in book["title"].lower():
        print("Book Found:")
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        found = True

if not found:
    print("Book not found")
```

---

## How It Works

1. A list of books is created
2. Each book is represented as a dictionary
3. The user enters a search term
4. The program loops through the book collection
5. If a matching title is found:
   - Book details are displayed
6. If no match exists:
   - A "Book not found" message is shown

---

## Example Run

### Input

```text
Enter book title to search: python
```

### Output

```text
Book Found:
ID: 1
Title: Python Basics
```

---

## Concepts Covered

- Lists
- Dictionaries
- Nested data structures
- Loops
- Search operations
- String manipulation

---

## Why This Program?

This project introduces real-world concepts such as:
- Inventory management
- Data lookup operations
- Record searching
- Structured data storage

These concepts are commonly used in:
- Library systems
- Product catalogs
- Employee databases
- Customer management applications

---

## Possible Improvements

- Add new books
- Delete books
- Update book information
- Search by ID
- Store data in a file
- Add book availability status

---

## Author

Daily Python Practice  
Library Book Search System
