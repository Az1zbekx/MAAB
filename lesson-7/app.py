from manager import TaskManager
from task import Task
from json_storage import JSONStorage
# from csv_storage import CSVStorage  # Uncomment if using CSV

def main():
    # Use desired format here (JSON or CSV)
    storage = JSONStorage("tasks.json")  # Switch to CSVStorage("tasks.csv") if needed
    manager = TaskManager(storage)

    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == '1':
                task = Task(
                    task_id=input("Enter Task ID: "),
                    title=input("Enter Title: "),
                    description=input("Enter Description: "),
                    due_date=input("Enter Due Date (YYYY-MM-DD): "),
                    status=input("Enter Status (Pending/In Progress/Completed): ")
                )
                manager.add_task(task)
                print("✅ Task added!")

            elif choice == '2':
                tasks = manager.view_tasks()
                if tasks:
                    for t in tasks:
                        print(f"{t.task_id}, {t.title}, {t.description}, {t.due_date}, {t.status}")
                else:
                    print("No tasks found.")

            elif choice == '3':
                task_id = input("Enter Task ID to update: ")
                updated = manager.update_task(
                    task_id,
                    title=input("New Title: "),
                    description=input("New Description: "),
                    due_date=input("New Due Date: "),
                    status=input("New Status: ")
                )
                print("✅ Updated!" if updated else "❌ Task not found.")

            elif choice == '4':
                task_id = input("Enter Task ID to delete: ")
                deleted = manager.delete_task(task_id)
                print("✅ Deleted!" if deleted else "❌ Task not found.")

            elif choice == '5':
                status = input("Enter status to filter by: ")
                filtered = manager.filter_tasks(status)
                if filtered:
                    for t in filtered:
                        print(f"{t.task_id}, {t.title}, {t.description}, {t.due_date}, {t.status}")
                else:
                    print("No matching tasks.")

            elif choice == '6':
                manager.save_tasks()
                print("✅ Tasks saved.")

            elif choice == '7':
                manager.load_tasks()
                print("✅ Tasks loaded.")

            elif choice == '8':
                print("👋 Goodbye!")
                break

            else:
                print("❌ Invalid choice.")
        except Exception as e:
            print(f"❌ Error: {e}")
if __name__ == "__main__":
    main()
