import tkinter as tk

# primary tkinter window
parent = tk.Tk()
parent.title( "Parent" )

# A child window can be created like so
child = tk.Toplevel( parent )
child.transient( parent )
child.title( "Child" )

# Note the reference to parent when child is created
# The transient method will guarantee the child will ALWAYS be in front of the parent
# Any number of children can be created for every parent

# Complex widgets that have many components require time to instantiate correctly
parent.update_idletasks()

# When a parent is destroyed so will the children

def closer( event ):
    parent.destroy()

# Widgets can be bound to keyboard or mouse inputs
parent.bind( "<Escape>", closer )

parent.mainloop()
