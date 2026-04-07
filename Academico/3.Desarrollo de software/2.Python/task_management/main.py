from functions import *
from storage import *
from data import tasks

def menu():
    while True:
        print("=== Task management ===")
        print("1. Add new task.")
        print("2. Show task.")
        print("3. Find task.")
        print("4. Update task.")
        print("5. Delete task.")
        print("6. Exit.")

        option = input("Choose an option >> ")

        if option == "1":
            add_task(tasks)
            save_data()
        elif option == "2":
            show_task(tasks)
        elif option == "3":
            find_task(tasks)
        elif option == "4":
            update_task(tasks)
            save_data()
        elif option == "5":
            delete_task(tasks)
            save_data()
        elif option == "6":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

# Load data before starting / Cargar datos antes de iniciar
load_data() 

# Run program
menu()  