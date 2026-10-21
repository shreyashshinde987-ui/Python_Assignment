'''
34. Check whether a string is palindrome.
'''
text = input("Enter a string: ")
clean = text.lower()

reverse = ""

for ch in clean:
    reverse = ch + reverse

if clean == reverse:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
