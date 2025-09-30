# Simple To-Do List App

tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Delete a task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def delete_task():
    if not tasks:
        print("\nNo tasks to delete!")
    else:
        view_tasks()
        task_num = int(input("\nEnter task number to delete: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted!")
        else:
            print("Invalid task number!")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
