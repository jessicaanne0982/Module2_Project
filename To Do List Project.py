print("\nWelcome to the TO-DO List Application! \
                \nMenu: \
                \n1. Add a task: \
                \n2. View tasks: \
                \n3. Mark a task as complete: \
                \n4. Delete a task: \
                \n5. Quit \
                \n"
)
  
user_tasks =[]
 
def add_task():
    while True:
            new_task_input = input("\nEnter the task you'd like to add to the To Do List: ")
            if new_task_input == "":
                print("OOPS! You forgot to enter your task!  Try again!! ")
            else:
                new_task_and_status = new_task_input.lower() + ": Incomplete"
                user_tasks.append(new_task_and_status)
                print(f"{new_task_input} has been added to the list.")
                continue_input = input("Would you like to add another task? (yes/no): ").lower()
                if continue_input != 'yes':
                    break

def view_tasks():
    if user_tasks == []:
        print("Your To Do List is empty!")
    else:
        print("\nThe tasks on your To Do List are: ")
        for task in user_tasks:
            print(task)
     
def complete_task():
    while True:
        completed_task_input = input("What task have you completed? ")
        completed_task_and_status = completed_task_input.lower() + ": Incomplete"
        if completed_task_and_status in user_tasks:  
            new_task_status = completed_task_and_status.replace("Incomplete", "COMPLETE!")
            user_tasks.remove(completed_task_and_status)
            user_tasks.append(new_task_status)
            print(completed_task_and_status.replace("Incomplete", "COMPLETE!"))
        else:
            print(f"{completed_task_input} was not found in the To Do List.")
        continue_input = input("Would you like to mark another task completed? (yes/no): ").lower()
        if continue_input != 'yes':
            break

def delete_task():
    while True:
        task_to_delete = input("Enter a task to delete: ").lower()
        completed_task_delete = task_to_delete + ": COMPLETE!"
        incomplete_task_delete = task_to_delete + ": Incomplete"
        if completed_task_delete in user_tasks:
            user_tasks.remove(completed_task_delete)
            print(f"You've removed {task_to_delete} from the To-Do List!")
        elif incomplete_task_delete in user_tasks:
            user_tasks.remove(incomplete_task_delete)
            print(f"You've removed {task_to_delete} from the To-Do List!")
        else:
            print(f"{task_to_delete} was not found in the To Do List.")
        continue_input = input("Would you like to delete another task? (yes/no): ").lower()
        if continue_input != 'yes':
            break
 
def quit_application():
    print("Thank you for using the To Do List Application!")
    
 
while True:
    try:
        user_input = int(input("\nChoose a menu option: \n"))

        if user_input == 1:
            add_task()        

        elif user_input == 2:
            view_tasks()

        elif user_input == 3:
            complete_task()
    
        elif user_input == 4:
            delete_task()

        elif user_input == 5:
            quit_application()
            break
        else:
            print("Invalid option! Enter a menu option from 1 to 5: ")
    
    except ValueError:
        print("Invalid data type. Please enter a number from the menu options!")
        continue


