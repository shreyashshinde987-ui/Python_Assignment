'''
48. Check whether number is strong number.
(A strong number is a number whose sum of factorials of its digits
 is equal to the number itself. Example: 145 = 1! + 4! + 5!)
'''
num = int(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number")
else:
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10

        # Factorial of the digit
        fact = 1
        for i in range(1, digit + 1):
            fact *= i

        total += fact
        temp //= 10

    if total == num:
        print(num, "is a strong number")
    else:
        print(num, "is not a strong number")
