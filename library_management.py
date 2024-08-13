library_data={}

def add_recoard(name,book,email):
    library_data[name]={"issued_books":book,"email":email}

class Library_recoard():
    def __init__(self,name,book,email):
        self.name=name
        self.book=book
        self.email=email
        add_recoard(self.name,self.book,self.email)

s1=Library_recoard("meet","the secret","meetrai101@gmail.com")
print(library_data)