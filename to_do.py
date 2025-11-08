import os
import json
from datetime import datetime

file_path = "tasks.json"

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        json.dump([], f)
       
with open(file_path, "r") as f:
    try:
        task = json.load(f)
    except json.JSONDecodeError:
        task=[]
print("tasks: ", task)

def to_do():
    
    while True:
        
        print(" What do you want to do today!?")
        print("1. Add a new task.")
        print("2. View all the tasks.")
        print("3. Update a task.")
        print("4. Delete a task.")
        print("5. Mark completion of a task.")
        print("6.Exit.")

        try:
            choice = int(input("Enter your choice(1-6): "))
        except ValueError:
            print("Invalid choice! Please enter a valid number.\n")
            continue

        
        if choice == 1:
            title = input("Enter the title of the task: ")
            due_date = input("Enter the due date (DD-MM-YYYY): ")

            try:
                datetime.strptime(due_date, "%d-%m-%Y")
            except ValueError:
                print("Invalid date format! Use DD-MM-YYYY.")
                continue

            task_id = 1 if not task else task[-1]["id"]+1
            task.append({"id":task_id,
                         "title":title,
                         "due_date":due_date,
                         "completed":False})
            print(f"'{title}' added to your task.\n")

            with open("tasks.json", "w") as f:
                json.dump(task, f, indent = 4)
        
        elif choice ==2:
            if not task:
                print("No task yet.")
            else:
            
                print("View options.")
                print("1. View all tasks.")
                print("2. View only completed tasks.")
                print("3. View only pending tasks.")
                
                try:
                    option = int(input("Enter your option(1-3): "))
                except ValueError:
                    print("Invalid Option! Please enter number 1,2 or 3.\n")
                    continue
                
                if option == 1:
                    print("All tasks.")
                    for i,t in enumerate(task):
                        print(f"{i+1}. ID: {t['id']}, Title: {t['title']}, Due Date: {t['due_date']}, Completed: {t['completed']}\n")

                elif option == 2:
                    print("Completed tasks.")
                    completed = [t for t in task if t['completed'] == True]
                    if not completed:
                        print("No task completed yet.\n")
                    else:
                        for i,t in enumerate(completed):
                            print(f"{i+1}. ID: {t['id']}, Title: {t['title']}, Due Date: {t['due_date']}, Completed: {t['completed']}\n")

                elif option == 3:
                    print("Pending tasks.")
                    pending = [t for t in task if t['completed'] == False]
                    if not pending:
                        print("No task pending yet.\n")
                    else:
                        for i,t in enumerate(pending):
                            print(f"{i+1}. ID: {t['id']}, Title: {t['title']}, Due Date: {t['due_date']}, Completed: {t['completed']}\n")

                else:
                    print("Invalid choice! choose between 1,2 or 3.\n")

            
        elif choice == 3:
            if not task:
                print("No task to update.\n")
            else:
                for i,t in enumerate(task):
                    print(f"{i+1}. ID: {t['id']}, Title: {t['title']}, Due Date: {t['due_date']}, Completed: {t['completed']}\n")
                try:
                    index = int(input("Enter task number to update: "))-1
                except ValueError:
                    print("Invalid choice! Please enter a valid number.\n")
                    continue
                if 0 <= index < len(task):
                    new_task = input("Enter the updated title: ")
                    task[index]['title'] = new_task
                    print("Task updated successfully.\n")
                else:
                    print("Invalid task number.\n")

            with open("tasks.json", "w") as f:
                json.dump(task, f, indent = 4)
        
        
        elif choice == 4:
            if not task:
                print("No task to delete yet.\n")
            else:
                for i,t in enumerate(task):
                    print(f"{i+1}. ID: {t['id']}, Title: {t['title']}, Due Date: {t['due_date']}, Completed: {t['completed']}\n")
                try:
                    index = int(input("Enter task number to delete: "))-1
                except ValueError:
                        print("Invalid choice! Please enter a valid number.\n")
                        continue                    
                
                if 0<=index < len(task):
                    removed = task.pop(index)
                    print(f" '{removed['title']}', deleted successfully.\n")
                else:
                    print("Invalid task number.")

            with open("tasks.json", "w") as f:
                json.dump(task, f, indent = 4)
        
        
        elif choice == 5:
            if not task:
                print("No task yet.\n")
            else:
                for i,t in enumerate(task):
                    print(f"{i+1}. ID: {t['id']}, Title: {t['title']}, Due Date: {t['due_date']}, Completed: {t['completed']}\n")
                try:
                    index = int(input("Enter task number to be mark completed: "))-1
                except ValueError:
                    print("Invalid choice! Please enter a valid number.\n")
                    continue
                if 0 <= index < len(task):
                    task[index]['completed'] = True
                    print("Task marked completed.\n")
                else:
                    print("Invalid task number.\n")

            with open("tasks.json", "w") as f:
                json.dump(task, f, indent = 4)
        
        
        elif choice == 6:
            print("Exiting the To-Do list. Have a great day!\n")
            break
        
        
        else:
            print("Invalid choice! choose numbers between 1 and 6.\n")
to_do()