
#  To-Do List App (Python)



## Author
Made by Salman — A Python developer.


---


##  Project Objective
A simple console-based **To-Do List Application** built with **Python** that allows users to manage daily tasks efficiently. The project uses **classes**, **functions**, and **file handling** for data persistence.

---

##  Features

- **Add Task** – Add a new task to the list.
- **View Tasks** – Display all tasks with their status (Pending/Done).
- **Mark as Done** – Mark a specific task as completed.
- **Delete Task** – Remove a task from the list.
- **Data Persistence** – Save and load tasks from a text file (`tasks.txt`).

---

##  How It Works

###  Class: `ToDoList`

Handles all task-related operations like adding, displaying, marking as done, and deleting tasks. All tasks are stored in memory and saved to a file called `tasks.txt`.

###  Main Functions

- `add_task()` – Gets user input and adds a task to the list.
- `view_tasks()` – Displays all tasks with a checkbox icon.
- `mark_done()` – Lets the user mark a task as completed.
- `delete_task()` – Removes a task based on its number.
- `save_tasks()` and `load_tasks()` – Handle file I/O for data persistence.

---

##  Example Output

```plaintext
1. Add Task  2. View Tasks  3. Mark as Done  4. Delete Task  5. Exit
Choice: 1
Enter new task: Complete Python project
✔ Task added!

--- To-Do List ---
1. Complete Python project [❌]

Choice: 3
Enter task number to mark as done: 1
✔ Task marked as done!

--- To-Do List ---
1. Complete Python project [✅]


