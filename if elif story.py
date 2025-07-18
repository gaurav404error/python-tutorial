name = input("type your name.")
print("welcome {name.title()}to the lost temple of bihar!")

answer= input("you reach an old temple.do you want to enter or stay outside?")

if answer.lower() == "enter":
   answer=input("you see two doors: one has a lion sign and one has a snake sign. which do you choose?")
   
if answer.lower()=="lion":
      print(" a real lion was waiting! you tired running but...game over")
elif answer.lower()=="snake":
     answer=input("you see a golden idol and a snake guarding it. try to take idol?")
if answer.lower()=="yes":
     print("the snake bites you. turns out it was cursed.game over")
elif answer.lower()=="no":
     print("smart choice! a secret door opens to treasure.you win!")
else:
     print("you froze in fear. a trapdoor opens and you're gone now game over")
els



    

      
 


