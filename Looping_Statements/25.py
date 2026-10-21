'''
25. Count consonants in a string.
'''
text = input("Enter a string: ")

count = 0

for ch in text.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1

print("Number of consonants:", count)
