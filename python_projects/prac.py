print("welcome to calculator")

def add(a,b):
    return a+b
def subract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("select the operators")
print("1.add")
print("2.subract")
print("3.multiply")
print("4.divide")

choice=input("enter(1/2/3/4):")

if choice in ('1','2','3','4'):
    try:


        num1=float(input("enter the number:",))
        num2=float(input("enter the number:",))

        if choice=='1':
            print("result:",add(num1,num2))
        elif choice=='2':
            print("result:",subract(num1,num2))
        elif choice=='3':
            print("result:",multiply(num1,num2))
        elif choice=='4':
            print("result:",divide(num1,num2))
    except ValueError:
            print("invalid info")

