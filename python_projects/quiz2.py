score=0
print("welcome to the quiz app")
print("what is capital of india ")
answer={ '1':'delhi','2':'hyderabad','3':'newyork','4':'bombay'}
choice=input("value enter 1/2/3/4")
if(choice=='1'):
    print("correct answer u recived 15cr")
    score+=1
else:
    print("your choice is wrong" )
#question2

print("where is hyderabad")
answer={'1':'delhi','2':'bombay','3':'keral','4':'telangana'}
choice=input("enter value in 1/2/3/4")
if(choice=='4'):
    print("correct answer u recived 15cr")
    score+=1
else:
    print("wrong choice u lost 15cr")

#question3

print("what is my name")
answer={'1':'brinda','2':'saanvi','3':'brutikaa','4':'nagalakshmi'}
choice=input("enter the choice in 1/2/3/4")
if(choice=='3'):
    print("ur answer is correct u recived 15cr")
    score+=1
else:
    print("invalid choice")

print("congratsyou completed ur quiz")
print("ur  final is score:",score,"out of 3")