def graterthen(num1,num2,num3):
    """function for gratee number between three numbers"""
    if(num1>num2):
        grater=num1
    elif(num2>num3):
        grater=num2
    else:
        grater=num3
    return grater
    
print(graterthen(70,800,90))

def sun(number):
    # function to find sun of array
    total=0
    for i in number:
        total+=i
    return total
print(sum((4,6,7,4,9,7,8)))


