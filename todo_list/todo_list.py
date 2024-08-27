import json
from tkinter import *
from tkinter import messagebox
import threading
import logging
logging.basicConfig()

try:
    with open ("todo_list\\todolist.json","r") as f:
        todolist=json.load(f)
except:
     todolist=[]

class Todolist:
    def __init__(self):
        
        self.addtaskroot=False
        self.viewtaskroot=False
        self.r_taskroot=False

    def on_addtask(self):
        self.addtaskroot=True
    def on_viewtask(self):
        self.viewtaskroot=True
    def on_remove_task(self):
        self.r_taskroot=True

to_do_list=Todolist()

def operations():
    while True:

        if to_do_list.addtaskroot:
            def addtask():
                newtask=e1.get()
                todolist.append(newtask)
                with open ("todo_list\\todolist.json","w") as f:
                    json.dump(todolist,f)
            print("hello ")
            add_root=Tk()
            add_root.title("to-do list")
            add_root.geometry("500x600+300+100")

            labl1=Label(add_root,text="welcome to todo list app")
            labl1.grid(row=1,column=1,sticky=N,ipadx=10,ipady=10,padx=170,pady=10)
            e1=Entry(add_root,text="add task")
            e1.grid(row=2,column=1)
            submit=Button(add_root,text="sibmit",width=10,height=2,command=addtask)
            submit.grid(row=3,column=1)
            to_do_list.addtaskroot=False
            add_root.mainloop()


        if to_do_list.on_viewtask:
            entry_text=""
            for index,values in enumerate(todolist,1):
                entry_text+=(f"{index}.{values}\n\n")

            root=Tk()
            root.title("to-do list")
            root.geometry("600x600+300+100")

            label=Label(root,text="this is the todo list",width=50,height=30)
            label.config(text=entry_text)
            label.grid(row=2,column=1)
            to_do_list.viewtaskroot=False


        if to_do_list.on_remove_task:
            def removetask():
                removebyindex=int(taskto_r.get())
                print(removebyindex)
                todolist.remove(todolist[removebyindex])
                print(todolist)
                with open ("todo_list\\todolist.json","w") as f:
                    json.dump(todolist,f)
            entry_text=""
            for index,values in enumerate(todolist):
                entry_text+=(f"{index}.{values}\n\n")
            root=Tk()
            root.title("to-do list")
            root.geometry("500x600+300+100")

            label=Label(root,text="this is the todo list")
            label.config(text=entry_text)
            label.grid(row=1,column=1)
            label=Label(root,text="choose index to remove from todo list")
            label.grid(row=2,column=1)
            taskto_r=Entry(root,text="add task")
            taskto_r.grid(row=3,column=1)
            submit=Button(root,text="sibmit",width=10,height=2,command=removetask)
            submit.grid(row=4,column=1)
            to_do_list.r_taskroot=False

thread1=threading.Thread(target=operations,daemon=True).start()


root=Tk()
root.title("to-do list")
root.geometry("500x600+300+100")

labl1=Label(root,text="welcome to todo list app")
labl1.grid(row=1,column=1,sticky=N,ipadx=10,ipady=10,padx=170,pady=10)

b1=Button(root,text="add task",width=10,height=2,command=to_do_list.on_addtask)
b1.grid(row=3,column=1)
b2=Button(root,text="view task",width=10,height=2,command=to_do_list.on_viewtask)
b2.grid(row=4,column=1)
b3=Button(root,text="remove task",width=10,height=2,command=to_do_list.on_remove_task)
b3.grid(row=5,column=1)

root.mainloop()

while True:
    pass

