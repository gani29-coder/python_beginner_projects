tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(num):
    if num < 1 or num > len(tasks):
        print("Invalid task number!")
    else:
        removed = tasks.pop(num - 1)
        print(f"Task '{removed}' deleted!")

while True:
    print("\nOptions: 1-Add Task, 2-View Tasks, 3-Delete Task, 4-Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        num = int(input("Enter task number to delete: "))
        delete_task(num)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")