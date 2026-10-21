'''
26. Print ASCII values of characters in a string.
'''
text = input("Enter a string: ")

for ch in text:
    print(ch, "->", ord(ch))
