loggedIn = False
username = ''

def title(): 
    print(""" 
   ||===========================||
   ||    Cart Tracker System    ||
   ||===========================||
""")
    
def choicePath(loggedIn, username):
    while True:
        choice = input("MENU: Enter your choice: ")
        if (loggedIn == True):
            value = cart_main(choice, loggedIn, username)
            if value == "exit":
                break
        else:
            value = auth_main(choice)
            if value == "exit":
                break
            elif value == "NF!":
                print("Credential not found")
                menu(loggedIn)
            elif value == "back-to-login":
                menu(loggedIn)
            else:
                username = value
                loggedIn = True
                print(f"\033[32m   Authenticated! Hello, {username}!   \033[0m")
                menu(loggedIn)

def viewUserCart(username):
    cart = open(f"cart_{username}.txt", "r")
    print("\033[33m|--------- Your Cart ---------|\033[0m")

    cartReadlines = cart.readlines()

    ice = 1
    try:
        if (cartReadlines[0]):
            pass
    except:
        print("\033[33m|       No cart item yet      |\033[0m")
        print("\033[33m|-----------------------------|\033[0m")
        return "no item"
    for i in cartReadlines:
        slicedString = i[0:len(i) - 1]
        print(f"""\033[33m         {ice}. {slicedString}\033[0m""")
        ice = ice + 1
    print("\033[33m|-----------------------------|\033[0m")
    cart.close() # ! NOT SURE    
    return cartReadlines

def createUserFile(username):
    try:
        open(f"cart_{username}.txt", "x")
    except:
        # ? if it throws error, it means that fiile alredy exist
        # ? proceed to # > 2
        pass

def cart_main(choice, loggedIn, username):
    createUserFile(username) # ? makes user has cart file
    if choice == '1':
        viewUserCart(username)
        menu(loggedIn)

    elif choice == '2':
        item = input("Enter item: ")
        cart = open(f"cart_{username}.txt", "a")
        cart.write(f"{item}\n")
        print(f"\033[32m\n   Item: \"{item}\" Successfully Added.  \033[0m")
        print(f"\033[32m       Enter '1' to view again   \n\033[0m")
        cart.close()
        menu(loggedIn)

    elif choice == '3':
        items = viewUserCart(username)
        if (items == "no item"):
           print(".  Add item first before removing an item.   ")
        else:
            toRemove = int(input("Which to delete? Enter number: ")) # ! need validation
            items.pop(toRemove - 1)
            cart = open(f"cart_{username}.txt", "w") # ? overwrite
            for i in items:
                cart.write(i)
        print(f"\033[32m\n   Successfully Removed!   \033[0m")
        print(f"\033[32m  Enter '1' to view again   \n\033[0m")
        menu(loggedIn)

    elif choice == 'exit':
        return "exit"
    else:
        print("Invalid input")        

def auth_main(choice):
    if choice == '1':
        users = open("users.txt", "r")
        username = input("Username: ")
        password = input("Password: ")
        usersString = users.read()
        usersList = usersString.split()
        
        for i in usersList:
            if (f"{username},{password}") in i:
                return username
            
        return "NF!"
        
    elif choice == '2':
        users = open("users.txt", "a")
        username = input("Username: ")
        password = input("Password: ")
        usersString = users.write(f"{username},{password} ")
        print(f"\033[32m\n       Successfully Registered!   \033[0m")
        print(f"\033[32m\n  You can now Log In below (option 1)!   \033[0m")
        return 'back-to-login'
    
    elif choice == 'exit':
        return 'exit'
    
    else:
        print("Invalid input")  
        return "back-to-login"      

def menu(loggedIn):
    if (loggedIn):
        print(""" 
    |---------------------------|          
    |           MENU            |      
    |---------------------------|
    |    1  |   View Cart       |
    |    2  |   Add Cart        |
    |    3  |   Remove Cart     |
    |---------------------------|
    |    type 'exit' to exit    | 
    |---------------------------|
""")
    else:
        print(""" 
    |---------------------------|          
    |     Login or Register     |      
    |---------------------------|
    |    1  |   Log In          |
    |    2  |   Register        |
    |---------------------------|
    |    type 'exit' to exit    | 
    |---------------------------|
""")

# > MAIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,
title()
menu(loggedIn)
choicePath(loggedIn, username)