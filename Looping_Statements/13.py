'''
13. Check whether a number is palindrome.
'''
num = int(input("Enter a number: "))

if num < 0:
    print(num, "is not a palindrome (negative number)")
else:
    temp = num
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    if num == reverse:
        print(num, "is a palindrome")
    else:
        print(num, "is not a palindrome")
