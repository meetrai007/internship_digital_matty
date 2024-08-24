import random
import logging

logging.basicConfig(level=logging.DEBUG)

word_list = [
    "apple", "banana", "cherry", "grape", "orange",
    "pineapple", "strawberry", "watermelon", "peach", "mango",
    "computer", "keyboard", "mouse", "monitor", "printer",
    "guitar", "piano", "violin", "drums", "trumpet",
    "mountain", "river", "ocean", "forest", "desert",
    "elephant", "tiger", "giraffe", "lion", "zebra",
    "house", "apartment", "castle", "cottage", "mansion",
    "bicycle", "car", "train", "airplane", "helicopter",
    "pencil", "book", "notebook", "backpack", "calculator",
    "pizza", "burger", "pasta", "sushi", "salad"
]
guess=random.choice(word_list)
chance=5
word="-" * (len(guess))

logging.info(f"guess the word:{word}")

while True:
    try:
        user_guess=str(input("\nEnter your guess alphabet:"))
    except:
        logging.error("Enter valid alphabet a-z")
        continue

    if user_guess in guess:
        new_word=""
        for i in range (len(guess)):
            if user_guess==guess[i]:
                new_word+=user_guess
            else:
                new_word+=word[i]
        word=new_word
        logging.info(f"current word:{new_word}")

    else:
        chance-=1
        logging.warning(f"entred wrord,your chanse left:{chance}")
        if chance==0:
            logging.info("you are loss the game")
            logging.info(f"Correct word is {guess}")
            break

    if guess==word:
        logging.info(f"you are win the game, with {chance} chanses")
        break
        
        

    