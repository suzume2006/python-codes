print("welcome to the quiz")
print("what is the full form of p.t.o")
value={'1':'please turn over','2':'please top open','3':'pop top open','4':'please tap over'}
choice=input("enter the choice 1/2/3/4")
try:

    if(choice=='1'):
        print("correct answer")
    elif(choice=='2'):
        print("incorrect answer")
    elif(choice=='3'):
        print("incorrect answer")
    elif(choice=='4'):
        print("incorrect answer")
    else:
        print("Invalid choice!")
except ValueError:
    print("invalid input")    
 


