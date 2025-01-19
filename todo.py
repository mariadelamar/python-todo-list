# todo.py - A simple command-line to-do list app

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f'Added: "{task}"')

def mark_done(task_number):
    if 1 <= task_number <= len(tasks):
        print(f'Marked "{tasks[task_number-1]}" as done.')
        del tasks[task_number-1]
    else:
        print("Invalid task number!")

while True:
    command = input("\nEnter command (add, show, done, quit): ").strip().lower()
    if command == "add":
        task = input("Enter task: ").strip()
        add_task(task)
    elif command == "show":
        show_tasks()
    elif command == "done":
        try:
            num = int(input("Enter task number: "))
            mark_done(num)
        except ValueError:
            print("Please enter a valid number.")
    elif command == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid command!")
