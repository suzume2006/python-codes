contact={}

def show_menu():
    print("\.list method")
    print("\1.add contact")
    print("\2.view contact")
    print("\3.search contact")
    print("\4.delete")
    print("\5exit")

def add_contact():
    name=input("enter the name")
    number=int(input("enter the number"))
    contact[name]=number
    print("contact added")

def view_contact():
    if not contact():
        print("contact not found")
        




