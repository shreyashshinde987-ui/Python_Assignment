'''
49. Write a program to print result status using match case.
'''
status = input("Enter result code (P = Pass, F = Fail, A = Absent, W = Withheld): ").upper()

match status:
    case "P":
        print("Result: Pass")
    case "F":
        print("Result: Fail")
    case "A":
        print("Result: Absent")
    case "W":
        print("Result: Withheld")
    case _:
        print("Invalid result code")
