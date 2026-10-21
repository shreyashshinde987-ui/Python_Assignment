'''
26. Write a program to check month names based on month number.
'''
month= int(input("Enter month number= "))
match month:
    case 1:
        print("Jan")
    case 2:
        print("Feb")
    case 3:
        print("Mar")
    case 4:
        print("Apr")
    case 5:
        print("May")
    case 6:
        print("Jun")
    case 7:
        print("jul")
    case 8:
        print("Aug")
    case 9:
        print("Sep")
    case 10:
        print("Oct")
    case 11:
        print("Nov")
    case 12:
        print("Dec")
    case _:
        print("Invalid Month")