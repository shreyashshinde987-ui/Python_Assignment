'''
Mini Project 2: Student Marks and Grade Report
'''
count = int(input("Enter number of students: "))

if count <= 0:
    print("Error: Number of students must be greater than 0")
else:
    total_marks = 0
    pass_count = 0
    fail_count = 0

    for i in range(1, count + 1):
        print(f"\n--- Student {i} ---")
        name = input("Enter student name: ")
        marks = float(input("Enter marks (0-100): "))

        # Reject marks outside 0-100
        while marks < 0 or marks > 100:
            print("Invalid marks! Marks must be between 0 and 100.")
            marks = float(input("Enter marks (0-100): "))

        if marks >= 75:
            grade = "A"
        elif marks >= 60:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "Fail"

        if grade == "Fail":
            fail_count += 1
        else:
            pass_count += 1

        total_marks += marks
        print(name, "-> Grade:", grade)

    average = total_marks / count

    print("\n----- CLASS SUMMARY -----")
    print("Class Average :", round(average, 2))
    print("Pass Count    :", pass_count)
    print("Fail Count    :", fail_count)
