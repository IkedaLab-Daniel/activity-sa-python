
loggedIn = True
username = 'ice'

def createUserFile(username):
    try:
        open(f"cart_{username}.txt", "x")
    except:
        # ? if it throws error, it means that fiile alredy exist
        # ? proceed to # > 2
        pass

def cart_main(choice):
    print('cart main')
    createUserFile(username) # ? makes user has cart file
    if choice == '1':
        cart = open(f"cart_{username}.txt", "r")
        print("|--------- Your Cart ---------|")
        cartReadlines = cart.readlines()

        ice = 1
        try:
            if (cartReadlines[0]):
                pass
        except:
            print("|       No cart item yet      |")
        for i in cartReadlines:
            slicedString = i[0:len(i) - 1]
            print(f"""         {ice}. {slicedString}""")
            ice = ice + 1
        print("|-----------------------------|")

    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == 'exit':
        print('Exit point here')
    else:
        print('Invalid input')

def auth_main():
    print('auth main')

def menu():
    print(""" 
   ||===========================||
   ||    Cart Tracker System    ||
   ||===========================||
""")
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

    choice = input("Enter your choice: ")
    if (loggedIn):
        cart_main(choice)
    else:
        auth_main(choice)


# > MAIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,
menu()