x = 100
y = 100
z = 100

while(True):

    choice = int(input("\nWould you like to: \n 1. View inventory levels for all products \n 2. Add inventory to a specific product \n 3. Reduce inventory for a specific product \n 4. Exit the application \n"))
    if choice == 1:
        print("Product x:", x)
        print("Product y:", y)
        print("Product z:", z)
    elif choice == 2:
        while(True):
            a = input("What product would you like to add? \n")
            b = int(input("How much would you like to add? \n"))
            if a == 'x':
                    x = x + b
                    print("The new level of product x is:", x)
            elif a == 'y':
                    y = y + b
                    print("The new level of product y is:", y)
            elif a == 'z':
                    z = z + b
                    print("The new level of product z is:", z)
            else:
                print("\nI'm sorry, one of those values was not recognized, please enter which product and the amount you would like to add")
            break
    elif choice == 3:
        while(True):
            c = input("What product would you like to reduce? \n")
            d = int(input("How much would you like to subtract? \n"))
            if c == 'x':
                    x = x - d
                    print("The new level of product x is:", x)
            elif c == 'y':
                    y = y - d
                    print("The new level of product y is:", y)
            elif c == 'z':
                    z = z - d
                    print("The new level of product z is:", z)
            else:
                print("\nI'm sorry, one of those values was not recognized, please enter which product and the amount you would like to subtract")
            break        
    elif choice == 4:
        print("Have a nice day!")
        break
    else:
        print("\n Im sorry, that value was not recognized! Please enter an integer from 1-4")
    



