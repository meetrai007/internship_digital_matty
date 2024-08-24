import random
import logging

logging.basicConfig(level=logging.INFO)

"""to pick a random number and store in guess"""
guess=random.randint(1,100)
logging.debug(guess)
user_guess=None
etempts=0

logging.info("welcome to the guess the number game\n")
while guess != user_guess :
    etempts +=1
    try:
        user_guess=int(input("guess a number between 1 to 100:"))
    except Exception as ex:
        logging.error(f"Enter a valid integer number between 1-100")
        continue
    if user_guess==guess:
        logging.info(f"congratulation, you guess the right number with {etempts} etempts")
    elif (guess - 2) <= user_guess <= (guess + 2):
        logging.info("you are so close")
    elif user_guess<guess:
        logging.info("your guess is to low")
    elif user_guess>guess:
        logging.info("your guess is to high")
    else:
        logging.warning("enter a valid number between 1-100")