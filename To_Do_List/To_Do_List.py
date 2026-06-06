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




1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter choice:  1
Enter task:  read python
Task added!

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter choice:  2

Tasks:
1. read python