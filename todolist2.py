#kasia chlebek
#todo list 2
todoList= []
#This function presents a menu of options that allows the viewer to see or alter a music to-do list
#This function does not use parameters
def ToDoList():
    print("welcome to your music to-do list")
    print("Options: \n1. Add Task \n2. View Current List \n3. Mark Task as Completed \n4. Remove Task \n5. Remove all tasks \n6. Sort alphabetically \n7. Print number of items on list \n8. Exit Program")
    task=int(input("what option would you like to choose?"))
    if task==1:
        add = (input("What would you like to add?"))
        todoList.append(add)
    elif task==2:
        print (todoList)
    elif task==3:
        new=input("What would you like to mark as complete?")
        mark=todoList.index(new)
        todoList[mark]=(new+" X")
    elif task==4:
        remove=(input("What would you like to remove?"))
        todoList.remove(remove)
    elif task==5:
        todoList.clear()
    elif task==6:
        todoList.sort()
    elif task==7:
        print(len(todoList))
    elif task==8:
        print("Exiting...")
        quit()
    else:
        print("Invalid input, restarting program...")
    ToDoList()
#main
ToDoList()


