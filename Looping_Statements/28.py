'''
28. Check whether a number is Armstrong.
'''
num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a non-negative number")
else:
    # Count the digits
    temp = num
    digits = 0
    while temp > 0:
        digits += 1
        temp //= 10
    if num == 0:
        digits = 1

    # Sum of each digit raised to the power of total digits
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
