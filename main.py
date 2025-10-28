loggedIn = False
username = ''

def title(): 
    print("\033[96m" + """ 
   ||===========================||
   ||    Cart Tracker System    ||
   ||===========================||
""" + "\033[0m")
    
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
                print("\033[31m   Credential not found / not matched   \033[0m")
                menu(loggedIn)
            elif value == "back-to-login":
                menu(loggedIn)
            else:
                username = value
                loggedIn = True
                print(f"\033[32m   Authenticated! Hello, {username}!   \033[0m")
                menu(loggedIn)

def viewUserCart(username):
    try:
        with open(f"cart_{username}.txt", "r") as cart:
            print("\033[33m    |--------- Your Cart ---------|\033[0m")
            
            cartReadlines = cart.readlines()
            
            if not cartReadlines:
                print("\033[33m    |       No cart item yet      |\033[0m")
                print("\033[33m    |-----------------------------|\033[0m")
                return "no item"
            
            for ice, item in enumerate(cartReadlines, 1):
                slicedString = item.rstrip('\n')
                print(f"""\033[33m         {ice}. {slicedString}\033[0m""")
            
            print("\033[33m    |-----------------------------|\033[0m")
            return cartReadlines
    except FileNotFoundError:
        print("\033    [33m|       No cart item yet      |\033[0m")
        print("\033    [33m|-----------------------------|\033[0m")
        return "no item"

def createUserFile(username):
    try:
        with open(f"cart_{username}.txt", "x") as cart:
            pass  # ? File create success, lesss go!
    except FileExistsError:
        # ? File already exists, which is fine
        pass

def cart_main(choice, loggedIn, username):
    createUserFile(username) # ? makes sure user has cart file
    if choice == '1':
        viewUserCart(username)
        menu(loggedIn)

    elif choice == '2':
        item = input("Enter item: ").strip()
        if not item:
            print("\033[31m   Item cannot be empty!   \033[0m")
        else:
            with open(f"cart_{username}.txt", "a") as cart:
                cart.write(f"{item}\n")
            print(f"\033[32m\n   Item: \"{item}\" Successfully Added.  \033[0m")
            print(f"\033[32m       Enter '1' to view again   \n\033[0m")
        menu(loggedIn)

    elif choice == '3':
        items = viewUserCart(username)
        if items == "no item":
            print("\033[33m   Add item first before removing an item.   \033[0m")
        else:
            try:
                toRemove = int(input("Which to delete? Enter number: "))
                if 1 <= toRemove <= len(items):
                    items.pop(toRemove - 1)
                    with open(f"cart_{username}.txt", "w") as cart:
                        for item in items:
                            cart.write(item)
                    print(f"\033[32m\n   Successfully Removed!   \033[0m")
                    print(f"\033[32m  Enter '1' to view again   \n\033[0m")
                else:
                    print(f"\033[31m   Invalid number! Please enter a number between 1 and {len(items)}.   \033[0m")
            except ValueError:
                print("\033[31m   Please enter a valid number!   \033[0m")
        menu(loggedIn)

    elif choice == 'exit':
        return "exit"
    else:
        print("\033[31m   Invalid input   \033[0m")        

def auth_main(choice):
    if choice == '1':
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if not username or not password:
            print("\033[31m   Username and password cannot be empty!   \033[0m")
            return "back-to-login"
        
        try:
            with open("users.txt", "r") as users:
                usersString = users.read()
                usersList = usersString.split()
                
                for user_entry in usersList:
                    if f"{username},{password}" == user_entry:
                        return username
                        
            return "NF!"
        except FileNotFoundError:
            print("\033[31m   No users registered yet. Please register first.   \033[0m")
            return "back-to-login"
        
    elif choice == '2':
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if not username or not password:
            print("\033[31m   Username and password cannot be empty!   \033[0m")
            return "back-to-login"
        
        if ',' in username or ',' in password:
            print("\033[31m   Username and password cannot contain commas!   \033[0m")
            return "back-to-login"
        
        # ? Check if username already exists
        try:
            with open("users.txt", "r") as users:
                usersString = users.read()
                usersList = usersString.split()
                for user_entry in usersList:
                    existing_username = user_entry.split(',')[0]
                    if username == existing_username:
                        print("\033[31m   Username already exists! Please choose a different one.   \033[0m")
                        return "back-to-login"
        except FileNotFoundError:
            pass  # ? File doesn't exist yet, which is fine ///
        
        with open("users.txt", "a") as users:
            users.write(f"{username},{password} ")
        print(f"\033[32m\n       Successfully Registered!   \033[0m")
        print(f"\033[32m\n  You can now Log In below (option 1)!   \033[0m")
        return 'back-to-login'
    
    elif choice == 'exit':
        return 'exit'
    
    else:
        print("\033[31m   Invalid input   \033[0m")  
        return "back-to-login"      

def menu(loggedIn):
    if (loggedIn):
        print("\033[36m" + """ 
    |---------------------------|          
    |           MENU            |      
    |---------------------------|
    |    1  |   View Cart       |
    |    2  |   Add Cart        |
    |    3  |   Remove Cart     |
    |---------------------------|
    |    type 'exit' to exit    | 
    |---------------------------|
""" + "\033[0m")
    else:
        print("\033[36m" + """ 
    |---------------------------|          
    |     Login or Register     |      
    |---------------------------|
    |    1  |   Log In          |
    |    2  |   Register        |
    |---------------------------|
    |    type 'exit' to exit    | 
    |---------------------------|
""" + "\033[0m")

# > MAIN <
title()
menu(loggedIn)
choicePath(loggedIn, username)
print("\033[32mGoodbye!\033[0m")