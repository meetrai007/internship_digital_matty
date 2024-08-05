import random

word_list=["hello","hii","computer"]
guess=random.choice(word_list)
chance=5
word="-" * (len(guess))

print(f"guess the word:{word}")

while True:

    user_guess=str(input("\nEnter your guess alphabet:"))

    if user_guess in guess:
        new_word=""
        for i in range (len(guess)):
            if user_guess==guess[i]:
                new_word+=user_guess
            else:
                new_word+=word[i]
        word=new_word
        print(f"current word:{new_word}")

    else:
        chance-=1
        print(f"entred wrord,your chanse left:{chance}")
        if chance==0:
            print("you are loss the game")
            break

    if guess==word:
        print("you are win the game")
        break
        
        

    