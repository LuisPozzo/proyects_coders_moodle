# Task Management System (Python)

## Description

This is a simple **console-based Task Management System** developed in Python.
It allows users to manage their daily tasks by performing basic operations such as creating, viewing, searching, updating, and deleting tasks.

The system also includes **data persistence using a JSON file**, so tasks are saved and loaded automatically between executions.

---

## How to Run the Program

1. Make sure you have **Python 3** installed on your system.

2. Download or clone this repository.

3. Open a terminal in the project folder.

4. Run the following command:

```bash
python main.py
```

5. Use the menu displayed in the console to interact with the system.

---

## Features

The system includes the following functionalities:

### Task Management

* Add new tasks
* View all tasks
* Search tasks by:
  * ID
  * Title
  * Status (Pending / Completed)
* Update existing tasks
* Delete tasks

### Data Persistence

* Tasks are stored in a `task.json` file
* Data is automatically loaded when the program starts
* Data is saved after creating, updating, or deleting tasks

### Data Structure

* Tasks are stored using:
  * Lists
  * Dictionaries

Each task contains:
* `id` (unique identifier)
* `title`
* `description`
* `priority` (high, medium, low)
* `status` (Pending or Completed)

---

## Project Structure

```bash
project/
│
├── main.py        # Main menu and program execution
├── functions.py   # Core functionalities (CRUD operations)
├── storage.py     # Data persistence (save/load JSON)
├── data.py        # Global task list
├── task.json      # Stored data (created automatically)
```
---

## Example of Use

### **Adding a task

```
--- ADD TASK ---
Enter title: Study Python
Enter description: Practice functions
Enter priority: high

Task added successfully!
```

### **Viewing tasks

```
--- TASK LIST ---
ID: 1 | Title: Study Python | Description: Practice functions | Priority: high | Status: Pending
```

### **Searching by status

```
--- FIND TASK ---
Enter status (pending/completed): pending
```

---

## Technologies Used

* Python 3
* JSON (for data storage)

---

## Notes

* The program runs entirely in the console.
* Input validation is implemented to prevent errors.
* The system ensures a clean and user-friendly interaction.

