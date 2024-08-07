import random
import logging

logging.basicConfig(level=logging.DEBUG)

word_list=["hello","hii","computer"]
guess=random.choice(word_list)
chance=5
word="-" * (len(guess))

logging.INFO(f"guess the word:{word}")

while True:
    try:
        user_guess=str(input("\nEnter your guess alphabet:"))
    except:
        logging.ERROR("Enter valid alphabet a-z")
        continue

    if user_guess in guess:
        new_word=""
        for i in range (len(guess)):
            if user_guess==guess[i]:
                new_word+=user_guess
            else:
                new_word+=word[i]
        word=new_word
        logging.INFO(f"current word:{new_word}")

    else:
        chance-=1
        logging.WARNING(f"entred wrord,your chanse left:{chance}")
        if chance==0:
            logging.I("you are loss the game")
            logging.I(f"Correct word is {guess}")
            break

    if guess==word:
        logging.I("you are win the game")
        break
        
        

    