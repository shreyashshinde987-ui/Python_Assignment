'''
Mini Project 10: Multiplication Table and Number Analyzer
'''
num = int(input("Enter a positive integer for the table: "))

if num <= 0:
    print("Error: Please enter a positive integer")
else:
    print("\nMultiplication table of", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

    start = int(input("\nEnter start of range: "))
    end = int(input("Enter end of range: "))

    if start > end:
        print("Error: Start cannot be greater than end")
    else:
        even_count = 0
        odd_count = 0
        total = 0

        for n in range(start, end + 1):
            total += n
            if n % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        print("\n----- RANGE ANALYSIS -----")
        print("Even Count   :", even_count)
        print("Odd Count    :", odd_count)
        print("Sum of Range :", total)
