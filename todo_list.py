"""
To-Do List CLI App: add, view, and remove tasks.
Tasks stay in memory while the program is running.
"""

def show_menu():
    """Display the available actions."""
    print("\n===== TO-DO LIST =====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")


def add_task(tasks):
    """Ask the user for a task and add it."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    """Show tasks with numbers."""
    if not tasks:
        print("Your to-do list is empty.")
        return
    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def remove_task(tasks):
    """Remove a task by its displayed number."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        number = int(input("Enter the task number to remove: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Removed task: {removed}")
        else:
            print("That task number does not exist.")
    except ValueError:
        print("Invalid input. Please enter a whole-number task number.")


def main():
    # The list stores tasks for this session.
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye! Your session has ended.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
