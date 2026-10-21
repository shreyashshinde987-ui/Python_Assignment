'''
19. Write a program to print the day name based on day number (1–7).
'''
d_num= int(input("Enter day number= "))
match d_num:
    case 1:
        print("Mon")
    case 2:
        print("Tue")
    case 3:
        print("Wed")
    case 4:
        print("Thu")
    case 5:
        print("Fri")
    case 6:
        print("Sat")
    case 7:
        print("Sun")
    case _:
        print("Day not exist")    