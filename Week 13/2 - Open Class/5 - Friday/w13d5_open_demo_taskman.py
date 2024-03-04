""" 
The below is simply an idea of what the task should look like and the description
might have something extra or it might have something left out. The full 
requirements are still the learners responsibility by referencing the learner
guide for this task. 
"""

#------------------------------------------------------------------------------ 
""" 
Create a program for a small business that can help it to manage tasks 
assigned to each member of the team. 
This program will work with two text files, user.txt and tasks.txt. 

<tasks.txt> stores a list of all the tasks that the team is working on.
This text file already contains data about two tasks. 
The data for each task is stored on a separate line in the text file. 
Each line includes the following data (separated by a comma and space) 
about a task in this order:
  ■ The username of the person to whom the task is assigned.
  ■ The title of the task.
  ■ A description of the task.
  ■ The date that the task was assigned to the user.
  ■ The due date for the task.
  ■ Either a "Yes" or "No" value that specifies if the task has been completed yet.

<user.txt> stores the username and password for each user that has permission 
to use the program (task_manager.py). 
This text file already contains one default user that has the username, "admin" 
and the password, "adm1n". 
The username and password for each user must be written to this file in the 
following format:
  ■ The username followed by a comma, a space and then the password.
  ■ One username and corresponding password per line.

The program should allow your users to do the following:
  ○ Login. 
    The user should be prompted to enter a username and password. 
    Valid usernames and passwords are stored in a text file called user.txt. 
    Display an appropriate error message if the user enters a username that is 
    not listed in user.txt or enters a valid username but not a valid password. 
    The user should repeatedly be asked to enter a valid username and password 
    until they provide appropriate credentials.
    The following menu should be displayed once the user has successfully logged in:
    -   Please select one of the following options :
    -   r - register User
    -   a - add task
    -   va - view all tasks
    -   vm - view my tasks
    -   e - exit
  ○ If the user admin chooses "r" to register a user, the user should be prompted 
    for the new username and password. 
    When the username is produced, test and make sure that this new username
    does not already exist in the list.
    The user should also be asked to confirm the password. 
    If the value entered to confirm the password matches the value 
    of the password, the username and password should be written to user.txt 
    in the appropriate format.
    No other users are aloud to register users.
  ○ If the user chooses "a" to add a task, the user should be prompted to enter 
    the username of the person the task is assigned to, the title of the task, 
    a description of the task and the due date of the task. The data about the 
    new task should be written to tasks.txt. The date on which the task is assigned 
    should be the current date. Also assume that whenever you add a new task, 
    the value that indicates whether the task has been completed or not is "No".
  ○ If the user chooses "va" to view all tasks, display the information for 
    each task on the screen in the format below.

    Task:               Assign initial tasks
    Assigned to:        admin
    Date assigned:      10 Oct 2019
    Due date:           25 Oct 2019
    Task completed:     No
    Task description:   Use task_manager.py to assign each team member with appropriate tasks
    
  ○ If the user chooses "vm" to view the tasks that are assigned to them, only 
    display all the tasks that have been assigned to the user, that is 
    currently logged-in, on the screen in the format above.
    Make sure that each task is displayed with a corresponding number which 
    can be used to identify the task.
    -   Allow the user to select either a specific task (by entering a number) 
        or input "-1" to return to the main menu.
    -   If the user selects a specific task, they should be able to choose to either :
        * mark the task as complete or 
        * edit the task. 
    -   If the user chooses to mark a task as complete, the "Yes"/"No" value that
        describes whether the task has been completed or not should be changed to "Yes". 
    -   If the user chooses to edit a task, the username of the person to whom 
        the task is assigned or the due date of the task can be edited. 
    -   The task can only be edited if it has not yet been completed.

*****************************************************
"""


