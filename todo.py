import json
import os

TODO_FILE = 'todo_list.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    tasks.append({'task': task, 'done': False})
    save_tasks(tasks)
    print(f"Added task: {task}")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "Done" if task['done'] else "Pending"
        print(f"{i}. {task['task']} [{status}]")

def mark_task_done(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        save_tasks(tasks)
        print(f"Task {task_number} marked as done.")
    else:
        print("Invalid task number.")

def delete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {task['task']}")
    else:
        print("Invalid task number.")

def show_menu():
    print("\nTo-Do List Application")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as done: "))
            mark_task_done(tasks, task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(tasks, task_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
