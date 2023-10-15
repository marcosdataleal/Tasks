def add_task(manager, task):
    manager.append(task)
    print("Task added successfully!")

def view_tasks(manager):
    if not manager:
        print("No tasks found.")
    else:
        print("Task List:")
        for index, task in enumerate(manager):
            print(f"{index + 1}. {task}")

def remove_task(manager, task_number):
    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(manager):
            removed_task = manager.pop(task_number - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

task_manager = []

while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task_manager, task)
    elif choice == "2":
        view_tasks(task_manager)
    elif choice == "3":
        task_number = input("Enter the task number you want to remove: ")
        remove_task(task_manager, task_number)
    elif choice == "4":
        print("Thank you for using Task Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
