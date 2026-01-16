from op import *


create_table()

def menu():
    print("1 - Show all tasks")
    print("2 - Show incomplete tasks")
    print("3 - Add a task")
    print("4 - Mark a task as done")
    print("5 - Delete a task")
    print("0 - Exit")

while True:
    menu()
    choice = input("Enter command: ")

    if choice == "1":
        print("\nALL TASKS:")
        tasks = show_all_tasks()
  
        if not tasks:
            print("No tasks yet.")


    elif choice == "2":
        print("\nINCOMPLETE TASKS:")
        tasks = show_not_comleted()
        if not tasks:
            print("No incomplete tasks.")
        # for t in tasks:
        #     print(f"{t[0]}: {t[1]}")

    elif choice == "3":
        task = input("Enter a new task: ")
        add_task(task)
        print("Task added!")

    elif choice == "4":
        try:
            task_id = int(input("Enter the ID of the task to mark as done: "))
            update_task_status(task_id)
            print("Task updated!")
        except ValueError:
            print("Please enter a valid ID!")

    elif choice == "5":
        try:
            task_id = int(input("Enter the ID"))
            delete_tasks(task_id)
            print("Task deleted!")
        except ValueError:
            print("Please enter a valid ID!")

    elif choice == "0":
        print("Bye!")
        break

    else:
        print("error")