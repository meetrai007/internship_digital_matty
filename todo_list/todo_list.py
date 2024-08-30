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
            add_root.config(bg="#d9ced0")

            labl1=Label(add_root,text="welcome to todo list app",bg="#d9ced0",fg="black",font="Times 20 italic bold",width=33)
            labl1.grid(row=1,sticky=N,ipady=20)
            # labl1.grid(row=1,column=1,pady=20,padx=150)
            labl2=Label(add_root,text="enter a task to add in todo list",font="bold",bg="#d9ced0",fg="black")
            labl2.grid(row=2,pady=40)
            e1=Entry(add_root,text="add task",width=25,font="bold")
            e1.grid(row=3,pady=5,ipadx=5,ipady=5)
            submit=Button(add_root,text="sibmit",width=20,height=2,fg="white",bg="#436af2",font="bold",command=addtask)
            submit.grid(row=4,pady=30)
            to_do_list.addtaskstate=False


        if to_do_list.viewtaskstate:
            entry_text=""
            for index,values in enumerate(todolist,1):
                entry_text+=(f"{index}.{values}\n\n")

            view_root=Toplevel()
            view_root.title("to-do list")
            view_root.geometry("500x600+300+100")
            view_root.config(bg="#d9ced0")

            labl1=Label(view_root,text="the task of todo list",bg="#d9ced0",fg="black",font="Times 20 italic bold",width=31)
            labl1.grid(row=1,sticky=N,ipadx=10,ipady=10)
            label=Label(view_root,text="this is the todo list",bg="#d9ced0",width=30,height=20,font="Times 14 bold")
            label.config(text=entry_text)
            label.grid(row=2,sticky=N)
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
            remove_root.config(bg="#d9ced0")

            label=Label(remove_root,text="Select task to remove from todo list",bg="#d9ced0",fg="black",font="Times 19 italic bold",width=40)
            label.pack()
            listbox=Listbox(remove_root,selectmode=MULTIPLE,height=10,width=30,bg="#d9ced0",fg="black",font="Times 19 italic")
            listbox.pack(pady=20)
            for item in todolist: 
                listbox.insert(END, item)
            submit=Button(remove_root,text="sibmit",width=20,height=2,fg="white",bg="#436af2",font="bold",border=0,command=removetask)
            submit.pack()
            to_do_list.r_taskstate=False

thread1=threading.Thread(target=operations,daemon=True).start()


root=Tk()
root.title("to-do list")
root.geometry("500x600+300+100")
root.config(bg="#d9ced0")

labl1=Label(root,text="welcome to todo list app",bg="#d9ced0",fg="black",font="Times 20 italic bold",width=33)
labl1.grid(row=1,sticky=N,ipady=20)

b1=Button(root,border=0,text="add task",width=20,height=2,fg="white",bg="#436af2",font="bold",command=to_do_list.on_addtask)
b1.place(x=150,y=150)
b2=Button(root,border=0,text="view task",width=20,height=2,fg="white",bg="#436af2",font="bold",command=to_do_list.on_viewtask)
b2.place(x=150,y=250)
b3=Button(root,border=0,text="remove task",width=20,height=2,fg="white",bg="#436af2",font="bold",command=to_do_list.on_remove_task)
b3.place(x=150,y=350)

root.mainloop()


