
loggedIn = False
choice = ''

def cart_main():
    print('cart main')
    if choice == '1':
        pass
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
        cart_main()
    else:
        auth_main()


# > MAIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,
menu()