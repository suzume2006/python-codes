import random

a=int(input("enter the value:",))

b=random.randint(1,100)
attempt=0

attempt+=1
if(a>b):
    print("a is more decreasr the number")
elif(a<b):
    print("b is more increase the number")
else:
    print("both are same ")