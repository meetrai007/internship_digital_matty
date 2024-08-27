from tkinter import *
from tkinter import messagebox
import json

try:
    with open ("todo_list\\todolist2.json","r") as f:
        todolist2=json.load(f)
except:
     todolist2=[]


def addtask():
    newtask=entry.get()
    todolist2.append(newtask)
    listbox.insert(END, newtask) 
    with open ("todo_list\\todolist2.json","w") as f:
        json.dump(todolist2,f)
    
def remove_item(): 
    selected_checkboxs = listbox.curselection() 
  
    for selected_checkbox in selected_checkboxs[::-1]: 
        listbox.delete(selected_checkbox) 
    del todolist2[selected_checkbox]
    with open ("todo_list\\todolist2.json","w") as f:
        json.dump(todolist2,f)

     


root=Tk()
root.geometry("400x500")
root.title("to-do-list")

l1=Label(root,text="to-do-list app",bg="gray",fg="white",width=10,height=2,font=8)
l1.pack(fill=BOTH)

l2=Label(root,text="add task",bg="gray",fg="white",width=11,height=1,font=8)
l2.place(x=50,y=80)

l3=Label(root,text="task list",bg="gray",fg="white",width=11,height=1,font=6)
l3.place(x=230,y=80)

entry=Entry(root,width=10,font=6)
entry.place(x=50,y=150)

b1=Button(root,text="add task",width=11,height=1,font=1,command=addtask)
b1.place(x=50,y=220)
b2=Button(root,text="remove task",width=11,height=1,font=1,command=remove_item)
b2.place(x=50,y=300)

listbox=Listbox(root,selectmode=MULTIPLE,height=20)
listbox.place(x=230,y=150)
for item in todolist2: 
    listbox.insert(END, item) 

root.mainloop()
        
