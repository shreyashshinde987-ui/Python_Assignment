'''
27. Write a program to check login status based on username and password.
'''
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login Successful")
else:
    print("Invalid Username or Password")