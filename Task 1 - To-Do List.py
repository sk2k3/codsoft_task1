tasks = []

def addTask(): 
    task = input("Please enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks: 
        print("There are no tasks in the list")
    else: 
        print("Current Tasks:")
        for index, task in enumerate(tasks): 
            print(f"Task #{index+1}.{task}")
            
def deleteTask(): 
    listTasks()
    try:
        taskToDelete = int(input("Enter the number of the task to delete"))
        if taskToDelete >=0 and taskToDelete <= len(tasks): 
            tasks.pop(taskToDelete-1)
            print(f"Task {taskToDelete} has been deleted")
        else: 
            print(f"Task #{taskToDelete} was not found")
    except:
        print("Invalid Input")
    




if __name__ == "__main__": 
    #Create a loop to run the app 
    print("Welcome to the to do list app")
    while True: 
        print("\n")
        print(" Please select one of the following options:")
        print("____________________________________________")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if (choice == "1"):
            addTask()
        
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif (choice == "4"):
            break
        else:
            print("Invalid input, please try again")
    
    print("Goodbye!")