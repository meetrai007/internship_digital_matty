def createfile(fname):
    """function to create now file"""
    try:
        with open (fname,'w') as w:
            # w.write("welcome\n")
            print(f"file {fname} created successfully")
    except Exception as er:
        print("Try again with a Different file name")

def readfile(fname):
    with open(fname,'r') as f:
        data=f.read()
        print(data)

def writefile(fname):
    with open(fname,'w')as f:
        f.write(str(input("Enter what you write in this file:")))

def appendfile(fname):
    with open(fname,'a')as f:
        f.write(str(input("Enter what you write in this file:")))

