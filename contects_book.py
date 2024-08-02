# from fileheandling import *

contects = {}
while True:
    userchoice = int(
        input(
            "welcome choose what you want to do \n1 add contect\n2 view all contents\n3 search contect\n4 remove contect\n5 exit\nyour choice is:"
        )
    )

    if userchoice == 1:
        while True:
            name = str(input("enter your name: "))
            phoneno = int(input("enter your number: "))
            email = str(input("enter your email: "))
            with open ("cotenctbook.txt",'a') as f:
                f.write(f"{name}\tphone:{phoneno},email:{email}\n")
            contects[name] = {"phone number": phoneno, "email": email}
            choice = str(input("you want to add more number y/n: "))
            if str.lower(choice) == "n":
                break
    
    if userchoice == 2:
        with open ("cotenctbook.txt",'r') as f:
            data=f.read()
            print(data)
        for name,detail in contects.items():
            print(name)
            for info_type,info_detail in detail.items():
                print(f"\t{info_type}:{info_detail}")

    if userchoice == 3:
        print("this feature under work")
        break
        # while True:
        #     n_search = str(input("enter name to search number: "))
        #     for k, v in contects[n_search].items():
        #         print(f"{k}={v}")
        #     addmore = str(input("you want to search another content y/n: "))
        #     if (str.lower(addmore)) == "n":
        # #         break

    if userchoice == 4:
        print("this feature under work")
        break
        # while True:
        #     rem_contect = str(input("enter name of content you want to delete: "))
        #     contects.pop(rem_contect)
        #     delmore = str(input("you want to search another content y/n: "))
        #     if (str.lower(delmore)) == "n":
        #         print(contects)
        #         break

    if userchoice == 5:
        break
