import os
import datetime 

###############################################CLASS_1
class Task:
    def __init__(self, description, is_complete=False, due_date=None, priority=None):

        self.description = description
        self.is_complete = is_complete
        self.due_date = datetime.datetime.strptime(due_date, "%d-%m-%Y") if due_date else None #<--<
        self.priority = priority



################################################CLASS_2
class ToDoList:
    def __init__(self):
        self.file = None
        self.tasks = []
        self.fileName = "My_Task_File.txt"
        self.loadTasks()

    def addTask(self, description):
        self.tasks.append(Task(description))
        print("----------------Your Task Is Added Successfully-----------------")
        while True:
            choice = input("Do you want simply to save the file? , then TYPE>-->(yes/no): ")
            choice = choice.lower()

            try:
                if choice == 'yes':
                    self.saveFile()
                    print("----------------Your Task is saved to text file Successfully!-----------------")
                    break
                elif choice == 'no':
                    print("---Warning[!], your data will be lost after exiting the program if you don't save it in the text file.---")
                    print("----------------cancelled!-----------------")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid choice. Please enter 'yes' or 'no'.")

    def completeTask(self, x):
        if x < len(self.tasks): #compared by length
            self.tasks[x].is_complete = True
            print("-------------------Your Task is marked as completed!-------------------")
            self.saveFile()
        else:
            print("Invalid Task Number")


    def viewTask(self):

        def read_text_file(filename):
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                    print(f"Content of {filename}:\n{content}")

            except FileNotFoundError:
                print(f"File '{filename}' not found in the directory.")

        # checking the existence of the file
        print("--------------<<<>>>--------------")
        print("--------------<<<:::WARNING[!]->[You cannot edit the existing / previous file which is from this current directory]:::>>>--------------")
        print("--------------<<<task Details:::>>>--------------")
        read_text_file("My_Task_File.txt")
        print("--------------<<<>>>--------------")

        if not self.tasks: #checks object exists or not
            print("--------------<<<>>>--------------")
            print("No tasks new to view!\nCreate a new task first and Try again!") #object must exist
            print("--------------<<<>>>--------------")
            return
        self.tasks.sort(key=lambda x: (x.due_date is None, x.due_date))
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. [{'X' if task.is_complete else ' '}] {task.description}") #mark i for task INDEX



    def sortTaskbyDueDate(self):
        self.tasks.sort(key=lambda x: (x.due_date is None, x.due_date))
        self.viewTask()

    def sortTaskbyPriority(self):
        self.tasks.sort(key=lambda x: (x.priority is None, x.priority))
        self.viewTask()

    def removeTask(self, index):
        if index < len(self.tasks): #compared by length
            print("----------------Check your Task-List before removing:----------------")
            self.viewTask()  # TASK_LIST_BEFORE<--<
            self.tasks.pop(index)
            print("-------------------Your Task Has Been Removed Successfully!-------------------")
            self.saveFile()
            print("\n----------------Latest Task-List:----------------")
            self.viewTask()  # TASK_LIST_AFTER<--<
        else:
            print("Invalid Task Number")

    def addPriority(self, index, priority):
        if index < len(self.tasks):
            self.viewTask()  # TASK_LIST_BEFORE<--<
            self.tasks[index].priority = priority
            print("------------------------Priority added to the task!------------------------")
            self.saveFile()
            print("\n----------------Latest Task-List:----------------")
            self.viewTask()  # TASK_LIST_AFTER<--<
        else:
            print("Invalid Task Number")

    def addDueDate(self, index, due_date):
        if index < len(self.tasks):
            self.tasks[index].due_date = datetime.datetime.strptime(due_date, "%d-%m-%Y")
            print("--------------------Due date added into the task--------------------")
            self.saveFile()
            print("\n----------------Latest Task-List:----------------")
            self.viewTask()  # TASK_LIST_AFTER<--<
        else:
            print("Invalid Task Number")


    def saveFile(self):
        try:
            with open(self.fileName, 'w') as file:
                i = 1 #i is for Task Index
                for task in self.tasks:
                    file.write(f"\n{i}.Task Description:\n{task.description}\n_\nTask Completion Status: {task.is_complete}\n_\nTask due date: {task.due_date}\n_\nTask Priority: {task.priority}\n")
                    i = i + 1
            print(f"Your Task List Saved To {self.fileName}")

        except Exception as e:
            print("\n", e, "\n ----------------YOUR TASK FILE CANNOT BE SAVED---------------------")
            print("----------------------Please, try again----------------------")

    def loadTasks(self):
        try:
            if os.path.exists(self.fileName):
                with open(self.fileName, 'r') as file:
                    for line in file:
                        description, is_complete, due_date, priority = line.strip().split(',')
                        self.tasks.append(
                            Task(description, is_complete == 'True', due_date if due_date != 'None' else None,
                                 int(priority) if priority != 'None' else None))
        except Exception as e:
            print("\n", e, "\n ----------------YOUR TASK FILE CANNOT BE LOADED---------------------")
            print("----------------Please, try again---------------------")

#######################################################MAIN
def main():
    toDoList = ToDoList()
    try:
        while True:

            def clear_screen():

                os.system('cls' if os.name == 'nt' else 'clear') #clears the terminal screen
            clear_screen()

            print("╔════════════════════════════════════╗")
            print("║                                    ║")
            print("║----------ToDo List Manager---------║")
            print("║                                    ║")
            print("║           by                       ║")
            print("║         Sarjat                     ║")
            print("║             Afsan                  ║")
            print("║                 Anika              ║")
            print("╠════════════════════════════════════╣")
            print("║                                    ║")
            print("║ 1.  Add a task                     ║")
            print("║ 2.  Complete a task by marking     ║")
            print("║ 3.  View to-do list                ║")
            print("║     sorted by Numerical            ║")
            print("║     order                          ║")
            print("║ 4.  View to-do list                ║")
            print("║     sorted by due date             ║")
            print("║ 5.  View to-do list                ║")
            print("║     sorted by priority             ║")
            print("║ 6.  Remove a task                  ║")
            print("║ 7.  Add priority to                ║")
            print("║     task                           ║")
            print("║ 8.  Add due date to                ║")
            print("║     task                           ║")
            print("║ 9. Exit                            ║")
            print("║ When extra operations are done,    ║")
            print("║ new data will be                   ║")
            print("║ added to the file automatically!   ║")
            print("╚════════════════════════════════════╝")

            choice = int(input("Enter your choice (1-9): "))

            if   choice == 1:
                task_description = input("\n>>>Enter task description: ")
                toDoList.addTask(task_description)

            elif choice == 2:
                task_number = int(input("Enter the task number to mark as complete: ")) - 1
                toDoList.completeTask(task_number)

                #####Numerical SORT
            elif choice == 3:
                toDoList.viewTask() #<--< FIX IT

                #####Due date based SORT
            elif choice == 4:
                toDoList.sortTaskbyDueDate()
                #####Priority based SORT
            elif choice == 5:
                toDoList.sortTaskbyPriority()
            elif choice == 6: #remove a task by number

                task_number = int(input("Enter the task number to remove: ")) - 1
                toDoList.removeTask(task_number)


            #elif choice == 7:
                #toDoList.saveFile() # saving here again overwrites the old or previous file thus causes dataloss!
                #print("----------------Your Task is saved to text file Successfully!-----------------")
                ################################################
            elif choice == 7:
                task_number = int(input("Enter the task number to add priority: ")) - 1
                print("1 means -> Hard \n2 means -> Medium \n3 means -> Low")
                priority = int(input("Enter the priority (1-3): "))
                toDoList.addPriority(task_number, priority)

            elif choice == 8: #add due date to task by task number
                task_number = int(input("Enter the task number to add a due date: ")) - 1
                due_date = input("Enter the due date (DD-MM-YYYY) , (Example: 18-07-2023), follow this format: ")
                toDoList.addDueDate(task_number, due_date)
                ################################################
            elif choice == 9:
                print("--------------<<<>>>--------------")
                print("........Exiting the program........")
                print("--------------<<<>>>--------------")
                break
            else:
                print("-------!!!INVALID!!!!<<<INPUT>>>----------")
                print("-------Back to MAIN <<<MENU>>>-------")
                print("--------------<<<>>>--------------")
                main()

    except Exception as e:
        print("\n<<<>>>Error details:<<<>>>\n", "||||", e, "||||\n", "<<<>>>Invalid input!!!<<<>>>\n<<<>>>Please try again!<<<>>>")
        main()


if __name__ == "__main__":
    main()
