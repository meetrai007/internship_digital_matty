# todolist=[]
while True:
    userchoice=int(input("welcome choose what you want to do \n1 add task\n2 view task\n3 remove task\nyour choice is:"))


    if userchoice==1:
        while True:
            newtask=str(input("enter your new task:"))
            # todolist.append(newtask)
            with open ("todolist.txt",'w') as f:
                f.write(f"{newtask}\n")
            y_n=str(input("Enter y to add more task n to exit"))
            if y_n=="n":
                break
        # print("our list is\n")  
        # for i in range (len(todolist)):
        #     print(todolist[i])

    if userchoice==2:
        with open ("todolist.txt",'r') as f:
            dolist=f.read()
            print(dolist)
        # for i in range (len(todolist)):
        #     print(todolist[i])

    # if userchoice==3:
    #     for i in range (len(todolist)):
    #         print(todolist[i])
    #     print("choose what you want to remove task 1 or 2 or 3  ")
    #     a=int(input("enter choice here:"))
    #     choice=a-1
    #     task=todolist[choice]
    #     todolist.remove(task)
    #     for i in range (len(todolist)):
    #         print(todolist[i])

    

    if userchoice==3:
        break
