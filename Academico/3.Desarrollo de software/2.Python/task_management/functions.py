def input_int(message:str) ->int:
    """
    Prompt the user to enter an integer until a valid one is entered.
    Args:
        message (str): On-screen message.
    Returns:
        int: Value numeber positive
    """
    while True:
        try:
            value = int(input(message)) 
            if value > 0:
                return value
            print("Invalid option. Please try again..\n")
        except ValueError:
            print("Invalid option. Please try again..\n")

def input_text(message:str)->str:
    """
    validate that the text is not empty
    Args:
        message (str): On-screen message.
    Returns:
        str: not empty string.
    """
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Error: The field cannot be empty.\n")

def print_task(task:dict):
    """
    Print a formatted task
    """
    print(f"ID: {task['id']} | Title: {task['title']} | "
          f"Description: {task['description']} | Priority: {task['priority']} | "
          f"Status: {'Pending' if task['status'] else 'Completed'}")

def add_task(task_list:list):
    """
    Create and Add a new task to the task list.
    Each task includes:
    - id (auto-incremental)
    - title
    - description
    - priority (high, medium, low)
    - status (True = Pending, False = Completed)

    Args:
        tasks_list: Lsit of tasks.
    """
    print("\n--- ADD TASK ---")
    task_id = len(task_list) +1
    title = input_text("Enter title: ")
    description = input_text("Enter a description: ")
    while True:
        priority = input_text("Enter priority [high | medium | low]: ")
        if priority in ["high","medium","low"]:
            break
        else:
            print("Invalid option. Enter -> High, -> medium or -> low.\n")
    
    status = True  # True = Pending | False = Completed. for default True.
    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "priority": priority,
        "status": status
    }

    task_list.append(task)
    print("Task added successfully!\n")

def show_task(task_list:list):
    """
    Show the list of tasks.
    Args:
        task_list (list) : List of the taks
    """
    print("\n--- TASK LIST ---")

    # Check if the list is empty / Validar si la lista está vacía
    if not task_list:
        print("Not tasks registered.\n")
        return

    # show task / mostrar tareas
    for task in task_list:
        print_task(task)
    print()

def find_task(task_list:list):
    """
    Search for a task by ID, title or status.     
    Args:
        task_list (list) : List of the tasks
    """
    print("\n--- FIND TASK ---")
    if not task_list:
        print("Not tasks available.\n")
        return
    
    print("1. Search by ID")
    print("2. Search by Title")
    print("3. Search by Status")

    option = input_int("Choose an option (1, 2 or 3): ")
    
    while option not in [1,2,3]:
        print("Invalid option. Try again.\n")
        option = input_int("Choose an option (1, 2 or 3): ")
    
    #Search by ID
    if option == 1:
        task_id = input_int("Enter ID: ")

        for task in task_list:
            if task["id"] == task_id: 
                        print("\nTask found:")
                        print_task(task)
                        print(f"")
                        return
        
    #Search by title
    elif option == 2:
        title = input_text("Enter Title: ").lower

        for task in task_list:
            if task["title"].lower() == title:
                print("\nTask found:")
                print_task(task)
                print(f"")
                return

    elif option == 3:
        while True:
            status_input = input("Enter status (pending/completed): ").lower().strip()
            if status_input in ["pending", "completed"]:
                break
            print("Invalid option. Use 'pending' or 'completed'.")

        status_value = True if status_input == "pending" else False
        
        for task in task_list:
            if task["status"] == status_value:
                print("\nTask found:")
                print_task(task)
                return
    
    print("task not found.\n")

# Update task / actualizar tareas
def update_task(task_list:list):
    """ 
    update a task
    Args:
        task_list (list) : List of the tasks
    """

    print("\n--- UPDATE TASK ---")
    if not task_list:
        print("No tasks available.\n")
        return

    task_id = input_int("Enter task ID: ")

    for task in task_list:
        if task["id"] == task_id:
            # Validaciones controladas (no sale hasta ser correctas)
            task["title"] = input_text("New title: ")
            task["description"] = input_text("New description: ")
            
            while True:
                
                priority = input_text("New priority [High | medium | low]: ").lower()
                if priority in ["high", "medium", "low"]:
                    task["priority"] = priority
                    break
                print("Error: enter High, medium or low.\n")

            while True:
                status_input = input("Completed? (yes/no): ").lower().strip()
                if status_input in ("yes", "no"):
                    task["status"] = False if status_input == "yes" else True
                    break
                print("Error: enter 'yes' or 'no'.")

            print("Task updated successfully!\n")
            return

    print("Task not found.\n")

def delete_task(task_list:list):
    """ 
    update a task
    Args:
        task_list (list) : List of the tasks
    """
    print("\n--- DELETE TASK ---")

    if not task_list:
        print("Not tasks available.\n")
        return

    task_id = input_int("Enter task ID: ")

    for task in task_list:
        if task["id"] == task_id:

            confirm = input_text("Are you sure? (yes/no): ").lower().strip()
           
            if confirm == "yes":
                task_list.remove(task)

                for i, task_items in enumerate(task_list, start=1):
                    task_items["id"] = i
                print("Task deleted.\n")
            else:
                print("Operation cancelled.\n")
            return
        
    print("task not found.\n")