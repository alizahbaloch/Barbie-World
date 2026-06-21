tasks=[]
def showTasks():
    if len(tasks)==0:
        print("No tasks found")
    else:
        num=1
        for i in tasks:
            print(str(num),".", i)
            num+=1

while True:
    print("1.Add task")
    print("2.View task")
    print("3.Remove task")
    print("4.exit")

    choice=int(input("Enter the num 1-4 you want:"))

    if choice==1:
        task=input("Enter task:")
        tasks.append(task)
        print("Task added")

    elif choice==2:
        showTasks()

    elif choice==3:
        showTasks()
        if len(tasks)>0:
          try:
            rem=int(input("Enter the task you want to remove:"))
            removed=tasks.pop(rem-1)
            print("Item removed: ", removed)
          except(ValueError, IndexError):
            print("Enter valid number")

    elif choice==4:
        print("goodbye!")
        break
    else:
        print("enter valid no from 1-4")
