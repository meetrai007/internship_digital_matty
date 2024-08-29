import json
from tkinter import *
from tkinter import messagebox
import threading
import logging
logging.basicConfig(level=logging.INFO)

try:
    with open ("todo_list\\todolist.json","r") as f:
        todolist=json.load(f)
except:
     todolist=[]

class Todolist:
    def __init__(self):
        
        self.addtaskstate=False
        self.viewtaskstate=False
        self.r_taskstate=False

    def on_addtask(self):
        self.addtaskstate=True
    def on_viewtask(self):
        self.viewtaskstate=True
    def on_remove_task(self):
        self.r_taskstate=True

to_do_list=Todolist()

def operations():
    while True:

        if to_do_list.addtaskstate:
            def addtask():
                newtask=e1.get()
                todolist.append(newtask)
                with open ("todo_list\\todolist.json","w") as f:
                    json.dump(todolist,f)
                e1.delete(0,END)
                messagebox.showinfo("information","a task added in todo list")
                add_root.destroy()
            logging.debug("hello ")
            add_root=Toplevel()
            add_root.title("to-do list")
            add_root.geometry("500x600+300+100")

            labl1=Label(add_root,text="welcome to todo list app",bg="gray",fg="white")
            labl1.grid(row=1,sticky=N,ipadx=10,ipady=10,padx=170,pady=10)
            labl1=Label(add_root,text="enter a task to add in todo list")
            labl1.grid(row=3,sticky=N,ipadx=10,ipady=10,padx=170,pady=10)
            e1=Entry(add_root,text="add task")
            e1.grid(row=4)
            submit=Button(add_root,text="sibmit",width=10,height=2,command=addtask)
            submit.grid(row=6)
            to_do_list.addtaskstate=False


        if to_do_list.viewtaskstate:
            entry_text=""
            for index,values in enumerate(todolist,1):
                entry_text+=(f"{index}.{values}\n\n")

            view_root=Toplevel()
            view_root.title("to-do list")
            view_root.geometry("500x600+300+100")

            labl1=Label(view_root,text="the task of todo list",bg="gray",fg="white")
            labl1.grid(row=1,sticky=N,ipadx=10,ipady=10,padx=170,pady=10)
            label=Label(view_root,text="this is the todo list",width=50,height=30)
            label.config(text=entry_text)
            label.grid(row=2)
            to_do_list.viewtaskstate=False


        if to_do_list.r_taskstate:
            def removetask():
                logging.debug("removebyindex")
                for i in listbox.curselection():
               
                    todolist.remove(listbox.get(i))
                with open ("todo_list\\todolist.json","w") as f:
                    json.dump(todolist,f)
                listbox.delete(0,END)
                for item in todolist: 
                    listbox.insert(END, item)
            
            logging.debug("entry_text")
            remove_root=Toplevel()
            remove_root.title("to-do list")
            remove_root.geometry("500x600+300+100")

            label=Label(remove_root,text="enter the index of task to remove from todo list",bg="gray",fg="white")
            label.pack()
            label=Label(remove_root,text="choose index to remove from todo list")
            label.pack()
            listbox=Listbox(remove_root,selectmode=MULTIPLE,height=10)
            listbox.pack()
            for item in todolist: 
                listbox.insert(END, item)
            submit=Button(remove_root,text="sibmit",width=10,height=2,command=removetask)
            submit.pack()
            to_do_list.r_taskstate=False

thread1=threading.Thread(target=operations,daemon=True).start()


root=Tk()
root.title("to-do list")
root.geometry("500x600+300+100")

labl1=Label(root,text="welcome to todo list app",bg="gray",fg="white")
labl1.grid(row=1,sticky=N,ipadx=10,ipady=10,padx=170,pady=10)

b1=Button(root,text="add task",width=10,height=2,command=to_do_list.on_addtask)
b1.grid(row=4)
b2=Button(root,text="view task",width=10,height=2,command=to_do_list.on_viewtask)
b2.grid(row=7)
b3=Button(root,text="remove task",width=10,height=2,command=to_do_list.on_remove_task)
b3.grid(row=10)

root.mainloop()


