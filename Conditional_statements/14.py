'''
14. Write a program to check whether a given character is uppercase or lowercase.
'''
ch = input("Enter a character: ")
if ch >= 'A' and ch <= 'Z':
    print("The character is Uppercase")
elif ch >= 'a' and ch <= 'z':
    print("The character is Lowercase")
else:
    print("The character is not an alphabet")
