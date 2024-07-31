taskList = {}

def addTasks(taskList, task): 
    taskNum = len(taskList) + 1
    taskList[taskNum] = task   

def deleteTasks(numDelete, taskList):
    if numDelete in taskList:
        del taskList[numDelete]
    else:
        print(f"Task number {numDelete} not found.")

def printTasks(taskList):
    if not taskList:
        print("No tasks available.")
    else: 
        print(taskList)
        for task_id, task in taskList.items():
            print(f"{task_id}: {task}")


def main():
    global taskList 
    answer = input("Type 'A' to add a task, 'D' to delete a task, or 'V' to view task list. ").strip()
    if (answer == "A"):
        task = input("Please enter your task: ")
        addTasks(taskList, task)
        printTasks(taskList)
    elif (answer == 'D'):
        printTasks(taskList)
        numDelete = int(input("Please input the number of which task you would like to delete: "))
        deleteTasks(numDelete, taskList)
        printTasks(taskList)
    elif (answer == 'V'):
        printTasks(taskList)
    else:
        print("Please enter a valid character.")

print("hello! welcome to the to do list manager.")
while True: 
    main() 


