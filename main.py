loggedIn = True
username = 'ice'
def title(): 
    print(""" 
   ||===========================||
   ||    Cart Tracker System    ||
   ||===========================||
""")

def viewUserCart():
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

def createUserFile(username):
    try:
        open(f"cart_{username}.txt", "x")
    except:
        # ? if it throws error, it means that fiile alredy exist
        # ? proceed to # > 2
        pass

def cart_main(choice):
    createUserFile(username) # ? makes user has cart file
    if choice == '1':
        viewUserCart()

    elif choice == '2':
        item = input("Enter item: ")
        cart = open(f"cart_{username}.txt", "a")
        cart.write(f"{item}\n")
        print(f"\033[32m   Item: \"{item}\" successfully added.   \033[0m")
        cart.close() # ! NOT SURE
    elif choice == '3':
       viewUserCart()

    elif choice == 'exit':
        print("Exit point")
    else:
        print("Invalid input")

def auth_main():
    print('auth main')

def menu():
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

    choice = input("MENU: Enter your choice: ")
    if (loggedIn):
        cart_main(choice)
    else:
        auth_main(choice)


# > MAIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,
title()
while True:
    menu()