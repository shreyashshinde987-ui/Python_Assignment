'''
49. Display menu-driven program using while loop.
'''
choice = 0

while choice != 5:
    print("\n------ MENU ------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice >= 1 and choice <= 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", a + b)
        elif choice == 2:
            print("Result:", a - b)
        elif choice == 3:
            print("Result:", a * b)
        else:
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: division by zero")
    elif choice == 5:
        print("Thank you! Exiting program.")
    else:
        print("Invalid choice. Please try again.")
