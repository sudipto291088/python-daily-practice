# To-Do List Manager in Python

## Overview

This program simulates a simple To-Do List Manager.

Users can:
- Add tasks
- View tasks
- Remove tasks
- Exit the application

The project demonstrates lists, loops, user input handling, and task management functionality.

---

## Code

```python
tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == "3":
        task = input("Enter task to remove: ")

        if task in tasks:
            tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
```

---

## How It Works

1. Tasks are stored in a list
2. The user selects an action from the menu
3. New tasks can be added
4. Existing tasks can be viewed
5. Tasks can be removed
6. The application runs until the user exits

---

## Example Run

### Input

```text
1
Learn Python

1
Practice Coding

2
```

### Output

```text
Tasks:
1. Learn Python
2. Practice Coding
```

---

## Concepts Covered

- Lists
- While loops
- Conditional statements
- enumerate()
- CRUD-style operations

---

## Why This Program?

This project introduces:

- Task management systems
- Interactive console applications
- Data storage and retrieval
- Basic productivity tools

These concepts are commonly used in:

- Task tracking apps
- Project management tools
- Productivity software
- Personal organizers

---

## Possible Improvements

- Mark tasks as completed
- Assign priorities
- Save tasks to a file
- Search tasks
- Add due dates

---

## Author

Daily Python Practice  
To-Do List Manager
