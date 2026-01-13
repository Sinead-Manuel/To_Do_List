### To DO LIST APPLICATION ###
print("Welcome to To-Do List App!")

# Initial list - user can add and delete tasks from here
todo_list = [{"task": "Make a project", "status": "incomplete"}]

def add_task():
    print("\nAdd A Task")

    task_name = input("Enter the task name: ")

    # Appends a new task to todo_list
    todo_list.append({"task": task_name, "status": "incomplete"})

    print("\nTask added successfully!")

def view_tasks():
    print("\n~ To Do List ~")

    # Displays all tasks in todo_list
    i = 1
    for task in todo_list:
        print(i, ":", task["task"], "|", task["status"])
        i += 1

def remove_task():
    print("\nRemove A Task")
    view_tasks()

    task_number = int(input("\nEnter the task number to remove: "))

    todo_list.pop(task_number - 1)

    print("\nTask removed successfully!")


# Main menu which reappears after an option is completed
while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    option = int(input("Choose a menu option: "))

    match option:
        case 1:
            add_task()
        case 2:
            view_tasks()
        case 3:
            remove_task()
        case 4:
            print("\nExiting the application. Goodbye!")
            break
        case _:
            print("\nInvalid option. Please choose a valid option.")