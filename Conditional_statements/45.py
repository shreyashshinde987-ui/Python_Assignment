'''
45. Write a program to print menu-based food selection using match case.
'''
print("----- FOOD MENU -----")
print("1. Pizza   - Rs. 250")
print("2. Burger  - Rs. 120")
print("3. Pasta   - Rs. 180")
print("4. Sandwich - Rs. 90")
print("5. Coffee  - Rs. 60")

choice = int(input("Enter your choice (1-5): "))

match choice:
    case 1:
        print("You selected Pizza. Price: Rs. 250")
    case 2:
        print("You selected Burger. Price: Rs. 120")
    case 3:
        print("You selected Pasta. Price: Rs. 180")
    case 4:
        print("You selected Sandwich. Price: Rs. 90")
    case 5:
        print("You selected Coffee. Price: Rs. 60")
    case _:
        print("Invalid choice")
