contact={}

def show_menu():
    print("\n contact book menu")
    print("1.add contact")
    print("2. view all the contacts")
    print("3.search the contacts")
    print("4.delete")
    print("5.exit")

def add_contact():
    name=input("enter the name:")
    number=input("enter the phone number:")
    contact[name]=number
    print("contact added")

def view_contact():
    if not contact:
        print("no contact found")

    else:
        print("\n--all contact--")
        for name,phone in contact.item():
            print(f"{name}:{phone}")

def search_contact():
    name=input("enter name to search:")
    if name in contact:
        print(f"{name}'s phone number is{contact[name]}")
    else:
        print("contact not found")

def delete_search():
    name=input("enter nameto delete:")
    if name in contact:
        del contact[name]
        print("contact not found")

while True:
    show_menu()
    choice=input("choose an option (1-5):")

    if choice=='1':
        add_contact()
    elif choice=='2':
        view_contact()
    elif choice=='3':
        search_contact()
    elif choice=='4':
        delete_search()
    elif choice=='5':
        print("good byee!!")
        break
    else:
        print("invalid option verify again")
