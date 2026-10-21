'''
17. Write a program to check grade based on marks (A, B, C, Fail).
'''
t_mark= int(input("Enter Marks= "))
if t_mark >= 90:
    print("A grade")
elif t_mark < 90 and t_mark >= 70:
    print("B grade")
elif t_mark < 70 and t_mark >= 40:
    print("C grade")
else:
    print("Fail")    
