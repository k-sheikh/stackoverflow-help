#=====importing libraries===========
'''This is the section where you will import libraries'''
import re
from datetime import datetime, timedelta
import fileinput
import os

#====Functions====
# Register new user
def reg_user():
    # User input for login and validation
    new_username = input("Please enter a new username: ")
    while new_username in username_list:
        new_username = input("Username not available. Please enter a new username: ")
    new_password = input("Please enter a new password: ")
    new_password_validation = input("Please re-enter your new password: ")

    # Logic to validate password
    while new_password_validation != new_password:
        print("The passwords do not match. Please try again.")
        new_password = input("Please enter a new password: ")
        new_password_validation = input("Please re-enter your new password: ")
    print(f"\nCongratulations, you have registered the new user '{new_username}'.\n")

    # Append new user to 'user.txt' file
    with open ("user.txt", "a", encoding = "utf-8") as f:
        f.write(f"\n{new_username}, {new_password}")

# Add a new task
def add_task():
    # User input for task entry fields
        task_user = input("\nEnter the username of the person whom the task is assigned to: ")
        task_title = input("Enter a title of the task: ")
        task_description = input("Enter a description of the task: ")
        task_duedate = input("Enter a due date for the task: ")
        today = datetime.today().strftime('%d %b %Y')
        task_complete = "No"
        print("\nYou have successfully added a new task.")

        # Append task to 'tasks.txt' file
        with open ("tasks.txt", "a", encoding = "utf-8") as f:
            f.write(f"\n{task_user}, {task_title}, {task_description}, {task_duedate}, {today}, {task_complete}")

# View all tasks
def view_all():
    # Read all tasks, delimit line by line and create a list to output all values
    with open ("tasks.txt", "r", encoding = "utf-8") as f:
        for line in f:
            line_items = re.split(r', |\n', line)
            underscore = "-" * 79
            print(f"\n{underscore}\nTask\t\t\t{line_items[1]}\nAssigned to:\t\t{line_items[0]}\nDate assigned:\t\t{line_items[3]}\nDue date:\t\t{line_items[4]}\nTask complete:\t\t{line_items[5]}\nTask description:\t{line_items[2]}\n{underscore}")

# View my tasks
def view_mine():
    # Read all tasks, delimit line by line and create a list to output specific values
    with open ("tasks.txt", "r", encoding = "utf-8") as f:
        
        # Create a counter for specific user tasks
        task_count = 0

        for line in f:
            line_items = re.split(r', |\n', line)
            underscore = "-" * 79

            # Add my tasks to counter
            if username.lower() == line_items[0].lower():
                task_count += 1

            # Verify only specific user tasks are shown
            if username.lower() == line_items[0].lower():
                print(f"\n{underscore}\nTask number:\t\t{task_count}\nTask\t\t\t{line_items[1]}\nAssigned to:\t\t{line_items[0]}\nDate assigned:\t\t{line_items[3]}\nDue date:\t\t{line_items[4]}\nTask complete:\t\t{line_items[5]}\nTask description:\t{line_items[2]}\n{underscore}")

                # Append task to temporary 'temp.txt' file
                with open ("temp.txt", "a", encoding = "utf-8") as f:
                    f.write(f"{line_items[0]}, {line_items[1]}, {line_items[2]}, {line_items[3]}, {line_items[4]}, {line_items[5]}\n")

    # Create temporary text file    
    with open ("temp.txt", "r", encoding = "utf-8") as f:
        select_task = int(input("Would you like to select a specific task? Type -1 to exit: "))
        if select_task == -1:
            pass
        else:
            # Change value to index
            selected_task = select_task - 1

            # Split text lines into list, select list item (task), split by ', '
            line_list = f.read().splitlines()
            original_item = (line_list[selected_task])
            original_item = original_item.split(", ")
            replaced_item = original_item[:]

            # Check if the task has already been completed
            if original_item[5] == "Yes":
                print("\nSorry, this task has already been completed.")
            else:
                
                # Menu to select edit option
                select_menu = input('''\nPlease select one of the following options:
        m\t- mark the task as complete
        ed\t- edit the task
        : ''').lower()

                # Logic for 'task completed' section
                if select_menu == "m":
                    # Change 'No' item to 'Yes'
                    replaced_item[5] = "Yes"
                
                    # Convert list to string
                    original_item_string = ", ".join(original_item)
                    replaced_item_string = ", ".join(replaced_item)

                    # Replace 'No' to 'Yes' in 'tasks.txt' file
                    with fileinput.FileInput("tasks.txt", inplace = True) as f:
                        for line in f:
                            if (original_item_string in line):
                                print(line.replace(original_item_string, replaced_item_string), end = "")
                            else:
                                print(line, end = "")
                    
                    # Print confirmation message to console
                    print("\nTask successfully marked as complete.")

                elif select_menu == "ed":

                    # Submenu to select edit option
                    select_submenu = input('''\nPlease select one of the following options:
    u\t- change the username of the person to whom the task is assigned
    d\t- edit the due date of the task
    : ''').lower()

                    # Logic for 'change assigned user' section
                    if select_submenu == "u":

                        # Enter the username of the new user
                        change_username = input("\nEnter the username of the new user: ")

                        # Check if the username entered is already the assigned user
                        if original_item[0].lower() == change_username.lower():
                            print(f"Error!!! The task is already assigned to {change_username}.")
                        else:
                            # Change the username in the list
                            replaced_item[0] = change_username

                            # Convert list to string
                            original_item_string = ", ".join(original_item)
                            replaced_item_string = ", ".join(replaced_item)

                            # Replace old username to new username in 'tasks.txt' file
                            with fileinput.FileInput("tasks.txt", inplace = True) as f:
                                for line in f:
                                    if (original_item_string in line):
                                        print(line.replace(original_item_string, replaced_item_string), end = "")
                                    else:
                                        print(line, end = "")
                            
                            # Print confirmation message to console
                            print(f"\nTask successfully assigned to {replaced_item[0]}.")

                    # Logic for 'edit due date' section
                    elif select_submenu == "d":

                        # Enter the new due date
                        change_duedate = input("Enter a new due date for the task: ")

                        # Check if the due date already exists
                        if original_item[3] == change_duedate:
                            print(f"Error!!! This due date for this task is already {change_duedate}.")
                        else:
                            # Change the duedate in the list
                            replaced_item[3] = change_duedate

                            # Convert list to string
                            original_item_string = ", ".join(original_item)
                            replaced_item_string = ", ".join(replaced_item)

                            # Replace old duedate to new duedate in 'tasks.txt' file
                            with fileinput.FileInput("tasks.txt", inplace = True) as f:
                                for line in f:
                                    if (original_item_string in line):
                                        print(line.replace(original_item_string, replaced_item_string), end = "")
                                    else:
                                        print(line, end = "")
                            
                            # Print confirmation message to console
                            print(f"\nTask due date successfully changed to {replaced_item[3]}.")
    
    # Remove 'temp.txt' file
    os.remove("temp.txt")

# Generate task report
def gen_task_report():
    pass

# Generate user report
def gen_user_report():
    pass

# Generate reports



#====Login Section====
with open ("user.txt", "r", encoding = "utf-8") as f:
        login_details = re.split(r', |\n', f.read())
        username_list = login_details[::2]
        password_list = login_details[1::2]

        username = input("Please enter your username: ")
        while username not in username_list:
            username = input("Username not found. Please try again: ")

        password = input("Please enter your password: ")
        while password not in password_list:
            password = input("Incorrect password. Please try again: ")

while True:

    # if statement for the user 'admin'
    if username == 'admin':
        
        # Menu for 'admin' with feature to register new users and view user and task stats
        menu = input('''\nPlease select one of the following options:
r\t- register user
a\t- add task
va\t- view all tasks
vm\t- view my tasks
gr\t - generate reports
s\t- view statistics
e\t- exit
: ''').lower()

        # Logic for 'register' section
        if menu == 'r':
            reg_user()
           
        # Logic for 'add task' section
        elif menu == 'a':
            add_task()

        # Logic for 'view all tasks' sections
        elif menu == 'va':
            view_all()

        # Logic for 'view my tasks' section
        elif menu == 'vm':
            view_mine()

        # Logic for 'generate reports' section
        elif menu == 'gr':

            # Declare counters
            total_tasks = 0
            total_completed = 0
            total_incompleted = 0
            total_overdue = 0

            # Read 'tasks.txt'
            with open ("tasks.txt", "r", encoding = "utf-8") as f:
                for line in f:
                    line_items = re.split(r', |\n', line)

                    # Count number of tasks
                    total_tasks += 1
                    # Count number of completed/incompleted tasks
                    if line_items[5] == "Yes":
                        total_completed += 1
                    elif line_items[5] == "No":
                        total_incompleted += 1
                    # Count number of incomplete and overdue tasks
                    duedate = datetime.strptime(line_items[3], '%d %b %Y').date()
                    today = datetime.today().strftime('%Y-%m-%d')
                    today = datetime.strptime(today, '%Y-%m-%d').date()
                    if line_items[5] == "No":
                        if duedate < today:
                            total_overdue += 1
            
            # Calculate percentages
            pct_completed = (total_completed / total_tasks) * 100
            pct_overdue = (total_overdue / total_tasks) * 100

            # Write 'task overview' text file
            with open ("task_overview.txt", "w", encoding = "utf-8") as f:
                f.write(f"Total number of tasks:\t\t {total_tasks}\n")
                f.write(f"Number of completed tasks:\t {total_completed}\n")
                f.write(f"Number of incompleted tasks:\t {total_incompleted}\n")
                f.write(f"Number of overdue tasks:\t {total_overdue}\n")
                f.write(f"Percentage of completed tasks:\t {pct_completed:.2f} %\n")
                f.write(f"Percentage of overdue tasks:\t {pct_overdue:.2f} %\n")

            # Declare counters
            total_users = []
            total_tasks = 0

            # Read 'user.txt'
            with open ("user.txt", "r", encoding = "utf-8") as f:
                # Total number of users
                for line in f:
                    line = line.strip().split(", ")
                    total_users.append(line[0])
            print(f"Total number of users: {len(total_users)}")

            # Read 'tasks.txt'
            with open ("tasks.txt", "r", encoding = "utf-8") as f:
                # Total number of tasks
                for line in f:
                    total_tasks +=1
                print(f"Total number of tasks: {total_tasks}")

            # Create empty dictionary with username keys
            user_tasks = {}
            for username in total_users:
                user_tasks.update({username:0})
            print(user_tasks)



        # Logic for 'view statistics' section
        elif menu == 's':

            # Read 'user.txt' file and count the number of lines
            with open ("user.txt", "r", encoding = "utf-8") as f:
                total_users = 0
                for line in f:
                    total_users += 1
                print(f"\nTotal number of users: {total_users}")

            # Read 'tasks.txt' file and count the number of lines
            with open ("tasks.txt", "r", encoding = "utf-8") as f:
                total_tasks = 0
                for line in f:
                    total_tasks += 1
                print(f"Total number of tasks: {total_tasks}")

        # Exit program        
        elif menu == 'e':
            print(f"\nGoodbye!!!")
            exit()

        # Option for accidental input
        else:
            print("You have made a wrong choice, Please Try again")
    
    # if statement for all other users
    else:

        # Limited menu for non-administrative users
        menu = input('''\nPlease select one of the following options:
a\t- add task
va\t- view all tasks
vm\t- view my tasks
e\t- exit
: ''').lower()

        # Logic for 'add task' section
        if menu == 'a':
            add_task()

        # Logic for 'view all tasks' sections
        elif menu == 'va':
            view_all()

        # Logic for 'view my tasks' section
        elif menu == 'vm':
            view_mine()

        # Exit program        
        elif menu == 'e':
            print(f"\nGoodbye!!!")
            exit()

        # Option for accidental input
        else:
            print("You have made a wrong choice, Please Try again")