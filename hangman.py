import random

world_list=["hello","hii","computer"]
guess=random.choice(world_list)
chance=5

for i in guess:
    print("-",end="")

while True:
    
    user_guess=str(input("\nEnter your guess alphabet"))

    for k in range (len(guess)):
        if user_guess==guess[k]:
            newworld=world[:k]+ user_guess +world[k:]
            
        
    print(newworld)
            
    chance-=1
    if chance==0:
        print("youare loss the game")
        break
    
    if guess==world:
        print("you are win the game")
        break
        
        

    