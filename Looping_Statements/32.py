'''
32. Calculate power of a number without using pow().
'''
base = float(input("Enter base: "))
exponent = int(input("Enter exponent (integer): "))

if base == 0 and exponent < 0:
    print("Error: 0 cannot be raised to a negative power")
else:
    result = 1
    for i in range(abs(exponent)):
        result *= base

    if exponent < 0:
        result = 1 / result

    print(base, "raised to the power", exponent, "=", result)
