'''
36. Find sum of numbers entered by user until 0 is entered.
'''
total = 0

num = int(input("Enter a number (0 to stop): "))

while num != 0:
    total += num
    num = int(input("Enter a number (0 to stop): "))

print("Sum of entered numbers:", total)
