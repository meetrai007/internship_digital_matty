"""import math tu use some mathmatic methods"""
import math

"""there are some functions to solve any equations"""
def multiply(a,b):
    """to multiply two numbers"""
    result=a*b
    return result

def addition(a,b):
    """to addition two numbers"""
    result=a+b
    return result

def divided(a,b):
    """to divides two numbers"""
    result=a/b
    return result

def subtract(a,b):
    """to subtract two numbers"""
    result=a-b
    return result

def square(a):
    """to find square of a number"""
    result=a*a
    return result

def squareroot(a):
    """to find squareroot"""
    result=math.sqrt(a)
    return result

"""input by user which task he want to be performed"""
print("1.multiply","2.addition","3.divide","4.subtract","5.square","6.squareroot",sep="\n")

"""to taking a valid choice by user"""
while True:
    try:
        choice=int(input("choose what do you want "))
        if (choice>=1 and choice<=6):
            break
        else:
            print("enter a valid choice between options 1 to 5")
    except ValueError:
        print("enter a number only between options 1 to 5 not any other alphabets or symbols")

"""to taking a valid data by user""" 
while True: 
    try:  
        """to brake loop"""
        if (choice>=1 and choice<=4):
            """taking 2 inputs by user"""
            a=int(input("enter 1st number ="))
            b=int(input("enter 2st number ="))
            break
    
        elif((choice==5 or choice==6)):
            """taking 1 input for square"""
            a=int(input("enter a number for square ="))
            break
    
        else:    
            print("enter a valid choice between options 1 to 6")
        break
    except ValueError as valerror:
        print("please enter a numbr only not any alphabet or others")
 
"""to perform action acording to user requirements"""
if (choice==1):
    print("the result is =",multiply(a,b))
elif (choice==2):
    print("the result is =",addition(a,b))
elif (choice==3):
    print("the result is =",divided(a,b))
elif (choice==4):
    print("the result is =",subtract(a,b))
elif (choice==5):
    print("the result is =",square(a))    
elif (choice==6):
    print("the result is =",squareroot(a))    
else:
    print("hello")



