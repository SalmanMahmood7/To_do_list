class ToDoList:
    FILE = "tasks.txt"

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.FILE, "r") as f:
                for line in f:
                    task, status = line.strip().split("|")
                    self.tasks.append({"task": task, "done": status == "done"})
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open(self.FILE, "w") as f:
            for task in self.tasks:
                status = "done" if task["done"] else "pending"
                f.write(f"{task['task']}|{status}\n")

    def add_task(self):
        task = input("Enter new task: ")
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()
        print("✔ Task added!\n")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.\n")
            return
        print("\n--- To-Do List ---")
        for i, task in enumerate(self.tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['task']} [{status}]")
        print()

    def mark_done(self):
        self.view_tasks()
        try:
            index = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index]["done"] = True
                self.save_tasks()
                print("✔ Task marked as done!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

    def delete_task(self):
        self.view_tasks()
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(self.tasks):
                removed = self.tasks.pop(index)
                self.save_tasks()
                print(f"✔ Task '{removed['task']}' deleted!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")


# Main loop
def main():
    todo = ToDoList()
    while True:
        print("1. Add Task  2. View Tasks  3. Mark as Done  4. Delete Task  5. Exit")
        choice = input("Choice: ")
        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.mark_done()
        elif choice == "4":
            todo.delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


main()
