'''
43. Write a program to print month days using match case.
'''
month = int(input("Enter month number (1-12): "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("This month has 31 days")
    case 4 | 6 | 9 | 11:
        print("This month has 30 days")
    case 2:
        year = int(input("Enter year: "))
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("February has 29 days (leap year)")
        else:
            print("February has 28 days")
    case _:
        print("Invalid month number")
