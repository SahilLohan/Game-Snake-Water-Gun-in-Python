# snake > water
# snake < Gun
# Gun < water


import random

print("\n****************This is snake--water--gun game****************\n\n") 
def winnerOutOf(c1,c2):
    if c1=="snake" and c2=="water": return "snake"
    if c2=="snake" and c1=="water": return "snake"
    
    if c1=="water" and c2=="gun": return "water"
    if c1=="gun" and c2=="water": return "water"
    
    if c1=="snake" and c2=="gun": return "gun"
    if c1=="gun" and c2=="snake": return "gun"

GameIsNotOver=3
choices=("snake","water","gun")


while(GameIsNotOver):
    print("--------------------------------------------------------------------")
    Human=input("Enter Your choice[snake/water/gun] : ")
    Human=Human.lower()
    if Human=="snake" or Human=="water" or Human=="gun":
        Computer=random.choice(choices)
        while Computer==Human:
            Computer=random.choice(choices)
        print(f"Computer have choosen            : {Computer}")
        
        if winnerOutOf(Human,Computer)==Human:
           print("You Won !!!!! Hureeee.... \n\n\n")
        else:
            print("You Lose !!!!!.... \n\n\n")
    else:
        print("\nInvalid Choice :) \n")
    GameIsNotOver-=1
    
print("************************************")  
print("**********Free Trial is over********\n")
print("Please Take our premium to play more :)\n\n\nJust kidding .. run the program again to play :)")
