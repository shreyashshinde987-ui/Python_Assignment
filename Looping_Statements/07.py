'''
7. Calculate factorial of a number using for loop.
'''
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial of", num, "is", fact)
