"""
Todo List Manager
------------------
A command-line todo app using a list of dictionaries.
Each task is a dict: {"title": str, "priority": "high"/"medium"/"low", "done": bool}
"""

tasks = []


def add_task():
    """Ask the user for a title and priority, then add a new task."""
    title = input("Enter task title: ").strip()

    while True:
        priority = input("Enter priority (high/medium/low): ").strip().lower()
        if priority in ("high", "medium", "low"):
            break
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

    task = {"title": title, "priority": priority, "done": False}
    tasks.append(task)
    print(f"Task '{title}' added.\n")


def view_tasks(task_list=None):
    """Display all tasks (or a given subset) with their status and priority."""
    # If no specific list is passed, use the full task list
    if task_list is None:
        task_list = tasks

    if not task_list:
        print("\nNo tasks to show.\n")
        return

    print("\n--- Tasks ---")
    for i, task in enumerate(task_list, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']} (Priority: {task['priority']})")
    print("-------------\n")


def mark_done():
    """Mark a task as done by its number in the list."""
    view_tasks()
    if not tasks:
        return

    try:
        num = int(input("Enter the task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print(f"Task '{tasks[num - 1]['title']}' marked as done.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def delete_task():
    """Delete a task by its number in the list."""
    view_tasks()
    if not tasks:
        return

    try:
        num = int(input("Enter the task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed['title']}' deleted.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def filter_by_priority():
    """Show only the tasks matching a chosen priority."""
    while True:
        priority = input("Enter priority to filter by (high/medium/low): ").strip().lower()
        if priority in ("high", "medium", "low"):
            break
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

    filtered = [task for task in tasks if task["priority"] == priority]

    if not filtered:
        print(f"\nNo tasks with priority '{priority}'.\n")
    else:
        print(f"\n--- Tasks with priority '{priority}' ---")
        view_tasks(filtered)


def main():
    print("=== Todo List Manager ===")

    while True:
        print("Menu:")
        print("  1. Add task")
        print("  2. View tasks")
        print("  3. Mark task as done")
        print("  4. Delete task")
        print("  5. Filter by priority")
        print("  6. Quit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            filter_by_priority()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.\n")


if __name__ == "__main__":
    main()