'''
32. Write a program to check whether a student is eligible for an exam (attendance + marks).
'''
attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter marks: "))

if attendance >= 75 and marks >= 35:
    print("Student is eligible for the exam")
else:
    print("Student is not eligible for the exam")