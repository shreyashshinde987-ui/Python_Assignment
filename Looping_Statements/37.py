'''
37. Print numbers until user enters a negative number.
'''
num = int(input("Enter a number (negative to stop): "))

while num >= 0:
    print("You entered:", num)
    num = int(input("Enter a number (negative to stop): "))

print("Negative number entered. Program ended.")
