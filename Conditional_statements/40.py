'''
40. Write a program to check whether a password is valid using nested if.
Rules: at least 8 characters, contains a digit, an uppercase letter
and a special character.
'''
password = input("Enter a password: ")

if len(password) >= 8:
    if any(ch.isdigit() for ch in password):
        if any(ch.isupper() for ch in password):
            if any(not ch.isalnum() for ch in password):
                print("Password is valid")
            else:
                print("Invalid: must contain a special character")
        else:
            print("Invalid: must contain an uppercase letter")
    else:
        print("Invalid: must contain a digit")
else:
    print("Invalid: must be at least 8 characters long")
