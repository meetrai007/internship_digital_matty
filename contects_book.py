# from fileheandling import *
import json
import logging

logging.basicConfig(level=logging.INFO)

with open ("contects.json","r") as file:
    try:
        contects=json.load(file)
    except:
        logging.error("json file is blank so assign dict in contents variable")
        contects={}
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
            contects[name]={"number":phoneno,"email":email}
            with open ("contects.json",'w') as f:
                json.dump(contects,f)
            contects[name] = {"phone number": phoneno, "email": email}
            choice = str(input("you want to add more number y/n: "))
            if str.lower(choice) == "n":
                break
    
    if userchoice == 2:
        for name,detail in contects.items():
            logging.info(name)
            for info_type,info_detail in detail.items():
                logging.info(f"\t{info_type}:{info_detail}")

    if userchoice == 3:
        while True:
            n_search = str(input("enter name to search number: "))
            for k, v in contects[n_search].items():
                logging.info(f"{k}={v}")
            addmore = str(input("you want to search another content y/n: "))
            if (str.lower(addmore)) == "n":
                break

    if userchoice == 4:
        logging.debug("this feature under work")
        while True:
            rem_contect = str(input("enter name of content you want to delete: "))
            contects.pop(rem_contect)
            delmore = str(input("you want to search another content y/n: "))
            if (str.lower(delmore)) == "n":
                logging.info(contects)
                break

    if userchoice == 5:
        break

logging.debug(contects)