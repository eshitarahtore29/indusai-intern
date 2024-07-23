import os

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f'Task "{task}" added.')

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to delete a task
def delete_task():
    view_tasks()
    if tasks:
        task_num = int(input("Enter the number of the task to delete: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task}" deleted.')
        else:
            print("Invalid task number.")

# Function to display the menu
def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

# Main loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":

    main()
