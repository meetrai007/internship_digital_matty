import tkinter as tk
def page1():
    for widget in content_frame.winfo_children():
        widget.destroy()
    p1=tk.Frame(content_frame,bg="blue",width=350,height=600)
    p1.pack(side=tk.LEFT)
def page2():
    for widget in content_frame.winfo_children():
        widget.destroy()
    p2=tk.Frame(content_frame,bg="orange",width=350,height=600)
    p2.pack(side=tk.LEFT)
def page3():
    for widget in content_frame.winfo_children():
        widget.destroy()
    p3=tk.Frame(content_frame,bg="black",width=350,height=600)
    p3.pack(side=tk.LEFT)
def page4():
    for widget in content_frame.winfo_children():
        widget.destroy()
    p4=tk.Frame(content_frame,bg="green",width=350,height=600)
    p4.pack(side=tk.LEFT)

mainwindow=tk.Tk()
mainwindow.title("switch frame")
mainwindow.geometry("500x600+100+100")

manu_frame=tk.Frame(mainwindow,bg="#dccfd1",width=150,height=600)
manu_frame.pack(side=tk.LEFT)
manu_frame.pack_propagate(0)
btn1=tk.Button(manu_frame,bd=0,text="button",width=10,height=2,command=page1)
btn1.place(x=40,y=80)
btn1=tk.Button(manu_frame,bd=0,text="button",width=10,height=2,command=page2)
btn1.place(x=40,y=160)
btn1=tk.Button(manu_frame,bd=0,text="button",width=10,height=2,command=page3)
btn1.place(x=40,y=240)
btn1=tk.Button(manu_frame,bd=0,text="button",width=10,height=2,command=page4)
btn1.place(x=40,y=320)
content_frame=tk.Frame(mainwindow,bg="green",width=350,height=600)
content_frame.pack(side=tk.LEFT)

mainwindow.mainloop()

