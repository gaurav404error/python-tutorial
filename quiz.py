print("welcome to my computer quiz!")
playing= input("do you want to play?")

if playing.lower() !="yes":
    quit()
print("okay! let's play:)")
score=0
answer= input("what does cpu stands for?")
if answer.lower()=="central processing unit":
    print('correct!')
    score +=1
else:
    print('incorrect!')
answer= input("what does gpu stands for?")
if answer.lower()=="graphics processing unit":
    print('correct!')
    score +1
else:
    print('incorrect!')
answer=input("what does ram stands for?")
if answer.lower()=="randam acess memory":
    print('correct!')
    score +1
else:
    print('incorrect!')
answer=input("who is the Prime minister of india?")
if answer.lower()=="narendra modi" or answer.lower()=="modi":
    print('correct!')
    score+1
else:
    print('incorrect!')
answer=input("what does rom stands for?")
if answer.lower()=="read only memory":
    print('correct!')
    score+1
else:
    print('incorrect!')
print(f"You got {score} questions correct!")
print(f"You got {(score / 4) * 100} %.")




