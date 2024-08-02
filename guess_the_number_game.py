import random

"""to pick a random number and store in guess"""
guess=random.randint(1,100)
user_guess=None
etempts=0

print("welcome to the guess the number game\n")
while guess != user_guess :
    etempts +=1
    try:
        user_guess=int(input("guess a number between 1 to 100:"))
    except Exception as ex:
        print("Enter a valid integer number between 1-100")
        continue
    if user_guess==guess:
        print(f"congratulation, you guess the right number with {etempts} etempts")
    elif (guess - 2) <= user_guess <= (guess + 2):
        print("you are so close")
    elif user_guess<guess:
        print("your guess is to low")
    elif user_guess>guess:
        print("your guess is to high")
    else:
        print("enter a valid number between 1-100")