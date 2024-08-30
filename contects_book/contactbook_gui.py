import tkinter as tk
def page1():
    for widget in content_frame.winfo_children():
        widget.destroy()
    p1=tk.Frame(content_frame,bg="#d9cfd1")
    p1.pack(side=tk.LEFT)
    btn1=tk.Button(p1,text="page 1 button")
    btn1.grid(row=1,column=5)
    label1=tk.Label(p1,text="page1",bg="#d9cfd1")
    label1.grid(row=2,column=1)
    label1=tk.Label(p1,text="page1",bg="#d9cfd1")
    label1.grid(row=3,column=2)
    label1=tk.Label(p1,text="page1",bg="#d9cfd1")
    label1.grid(row=4,column=3)
def page2():
    for widget in content_frame.winfo_children():
        widget.destroy()
    p2=tk.Frame(content_frame,bg="#d9cfd1",width=350,height=600)
    p2.pack(side=tk.LEFT)
    label1=tk.Label(p2,text="page2",bg="#d9cfd1")
    label1.pack()
def page3():
    for widget in content_frame.winfo_children():
        widget.destroy()
    p3=tk.Frame(content_frame,bg="#d9cfd1",width=350,height=600)
    p3.pack(side=tk.LEFT)
def page4():
    for widget in content_frame.winfo_children():
        widget.destroy()
    p4=tk.Frame(content_frame,bg="#d9cfd1",width=350,height=600)
    p4.pack(side=tk.LEFT)

mainwindow=tk.Tk()
mainwindow.title("switch frame")
mainwindow.geometry("500x600+100+100")

manu_frame=tk.Frame(mainwindow,bg="#777378",width=150,height=600)
manu_frame.pack(side=tk.LEFT)
manu_frame.pack_propagate(0)
btn1=tk.Button(manu_frame,bd=0,text="button",width=7,height=1,fg="white",bg="#436af2",font="bold",command=page1)
btn1.place(x=40,y=80)
btn1=tk.Button(manu_frame,bd=0,text="button",width=7,height=1,fg="white",bg="#436af2",font="bold",command=page2)
btn1.place(x=40,y=160)
btn1=tk.Button(manu_frame,bd=0,text="button",width=7,height=1,fg="white",bg="#436af2",font="bold",command=page3)
btn1.place(x=40,y=240)
btn1=tk.Button(manu_frame,bd=0,text="button",width=7,height=1,fg="white",bg="#436af2",font="bold",command=page4)
btn1.place(x=40,y=320)
content_frame=tk.Frame(mainwindow,bg="#d9cfd1",width=350,height=600)
content_frame.pack(side=tk.LEFT)

mainwindow.mainloop()
