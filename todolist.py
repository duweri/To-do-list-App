TASKS_FILE = "tasks.txt" # This is a variable holding the filename

try: 
    with open(TASKS_FILE, "r", encoding="utf-8") as f: #opens the file for reading. "r" is read more and fails if non-existent. encoding="utf-8": makes reading text reliable across systems. with ... as f: is a context manager. It automatically closes the file when the block ends (even if an error happens). No need to call f.close() manually.
        tasks = [line.strip() for line in f] #line.strip() removes \n (new lines) at the end of each line.
except FileNotFoundError: #If the file doesn’t exist yet, the except block makes sure the program still works (starting with an empty list
    tasks = []
print("Welcome to your To-do list App!")
while True: 

    #Print menu 
    menu_options = ["1. View tasks", "2. Add task", "3. Delete task", "4. Quit"]

    for option in menu_options: # This goes throigh each item in the list and prints it one at a time
        print(option)
        
    choice = input("What task would you like to perform today?").strip() #this removes any extra spaces or invisible characters
    
    if choice == "4":
        print("Goodbye")
        break
    elif choice == "1":
        if not tasks: # This means if "the list is empty"
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1): #enumerate so each task gets a number 
                print(f"{i}) {task}") # how the tasks will be displayed with the number index and the task
        input("\nPress Enter to return to the menu...")
        continue

    elif choice == "2":
        # ADD TASK (we'll implement next)
        print("Add task selected (Step 4 will implement this).")
        input("\nPress Enter to return to the menu...")
        continue

    elif choice == "3":
        # DELETE TASK (we'll implement next)
        print("Delete task selected (Step 5 will implement this).")
        input("\nPress Enter to return to the menu...")
        continue

    else:
        print("Please choose a number between 1 and 4.")
        # no pause needed here, but you can add one if you like
        continue
    
 