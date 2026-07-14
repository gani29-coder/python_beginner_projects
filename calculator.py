tasks = []

def show_tasks():
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    
    print("\nOptions: 1-Add Task, 2-View Tasks, 3-Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
