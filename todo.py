
# while True:
#     userchoice=int(input("welcome choose what you want to do \n1 add task\n2 view task\n3 exit\nyour choice is:"))

#     if userchoice==1:
#         while True:
#             newtask=str(input("enter your new task:"))
#             with open ("todolist2.txt",'a') as f:
#                 f.write(f"{newtask}\n")
#             y_n=str(input("Enter y to add more task n to exit:"))
#             if y_n=="n":
#                 break
  
#     if userchoice==2:
#         with open ("todolist2.txt",'r') as f:
#             dolist=f.read()
#             print(dolist)
#             break

#     if userchoice==3:
#         break
import json
with open("todolist.txt","r") as file:
    dat=file.read()
    data=json.loads(dat)
print(data)