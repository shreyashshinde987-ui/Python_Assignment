'''
38. Write a program to check whether a student passed all subjects.
'''
pass_marks = 35

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

if maths >= pass_marks and science >= pass_marks and english >= pass_marks:
    print("Student passed all subjects")
else:
    print("Student did not pass all subjects")
