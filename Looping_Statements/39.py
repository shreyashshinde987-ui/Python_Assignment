'''
39. Count total words in a string.
'''
text = input("Enter a string: ")

count = 0

for word in text.split():
    count += 1

print("Total words:", count)
