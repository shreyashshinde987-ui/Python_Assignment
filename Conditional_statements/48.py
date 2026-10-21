'''
48. Write a program to print language choice using match case.
'''
print("Choose a language:")
print("1. English")
print("2. Hindi")
print("3. Marathi")
print("4. Spanish")

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print("You selected English: Hello")
    case 2:
        print("You selected Hindi: Namaste")
    case 3:
        print("You selected Marathi: Namaskar")
    case 4:
        print("You selected Spanish: Hola")
    case _:
        print("Invalid language choice")
