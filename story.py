# Desi Temple Adventure Game

name = input("Type your name: ")
print(f"Welcome {name.title()} to the Lost Temple of Bihar!")

answer = input("You reach an old temple. Do you enter or stay outside?")

if answer.lower() == "enter":
    answer = input("You see two doors: one has a lion sign  and one has a snake sign . Which do you choose?")

    if answer.lower() == "lion":
        print("A real lion was waiting! You tried running but... Game Over ")
    elif answer.lower() == "snake":
        answer = input("You see a golden idol and a snake guarding it. Try to take idol? (yes/no):")
        
        if answer.lower() == "yes":
            print("The snake bites you. Turns out it was cursed. Game Over ")
        elif answer.lower() == "no":
            print("Smart choice! A secret door opens to treasure. You win! ")
        else:
            print("You froze in fear. A trapdoor opens and you're gone! ")
    else:
        print("Wrong door. You fall into a pit. Game Over ")

elif answer.lower() == "stay":
    answer = input("You rest under a tree. Do you explore nearby or sleep? ")
    
    if answer.lower() == "explore":
        print("You find an old sadhu who gives you the temple map. You return rich!")
    elif answer.lower() == "sleep":
        print("You wake up in a monkey camp. They stole your phone. Game Over")
    else:
        print("You did nothing... and a wild bull chased you home.")

else:
    print("You wander off and get lost in the jungle. Game Over") 


