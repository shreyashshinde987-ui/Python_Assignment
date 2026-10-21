'''
24. Write a program to check exam results (Distinction, First Class, Pass, Fail).
'''
marks = float(input("Enter your percentage: "))

if marks >= 85 and marks <= 100:
    print("Distinction")
elif marks >= 65 and marks < 85:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")