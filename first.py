tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def show_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
