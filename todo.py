### To DO LIST APPLICATION ###
print("Welcome to To-Do List App!")

# Initial list - user can add and delete tasks from here
todo_list = [{"task": "Make a project", "status": "incomplete"}]

# Main menu which reappears after an option is completed
while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    option = input("Choose a menu option: ")

    match option:
        case '1':

            print("\nAdd A Task")

            task_name = input("Enter the task name: ")

            # Appends a new task to todo_list
            todo_list.append({"task": task_name, "status": "incomplete"})

            print("\nTask added successfully!")

        case '2':

            print("\n~ To Do List ~")

            # Displays all tasks in todo_list
            for task in todo_list:
                print(task["task"], "|", task["status"])

        case '3':
            print("\nRemove A Task")
        case '4':
            print("\nExiting the application. Goodbye!")
            break
        case _:
            print("\nInvalid option. Please choose a valid option.")