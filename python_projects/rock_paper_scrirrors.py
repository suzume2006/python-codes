import random
print("welcome to the world of nostalgia")
score=0
opponent=random.choice (['rock','paper','scrirrors'])

player=input("enter in rock/paper/scrirrors:").lower()

if(player=='rock' and opponent=='scrirrors'):
    print("you won!!")
    score+=1
elif(player=='rock' and opponent=='paper'):
    print("you lost~~")
elif(player=='rock' and opponent=='rock'):
    print("its a tie play again")
elif(player=='paper'and opponent=='scrirrors'):
    print("you lost ")
elif(player=='paper'and opponent=='rock'):
    print("you won!!")
    score+=1
elif(player=='paper' and opponent=='paper'):
    print("its a tie")
elif(player=='scrirrors' and opponent=='rock'):
    print("you lost~~")
elif(player=='scrirrors' and opponent=='paper'):
    print("you won!!")
    score+=1
elif(player=='scrirrors' and opponent=='scrirrors'):
        print("its a tie play again")
else:
     print("wrong input")