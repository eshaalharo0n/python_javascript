# A school wants to automate the process of calculating student results.
# Write a program in Python that takes a student's information and generates a result card showing the total marks, percentage, grade, and pass/fail status.

name = input("Enter your name: ")
sub1 = int(input("Enter your first subject marks (0-100): "))
sub2 = int(input("Enter your second subject marks (0-100): "))
sub3 = int(input("Enter your third subject marks (0-100): "))
sub4 = int(input("Enter your fourth subject marks (0-100): "))
sub5 = int(input("Enter your fifth subject marks (0-100): "))

if not (0 <= sub1 <= 100 and
        0 <= sub2 <= 100 and
        0 <= sub3 <= 100 and
        0 <= sub4 <= 100 and
        0 <= sub5 <= 100):
    print("Invalid marks! All marks must be between 0 and 100.")
else:
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 500 * 100

    print("Student name:", name)
    print("Total marks:", total, "/ 500")
    print(f"Percentage: {percentage:.2f}%")

    if 90 <= percentage <= 100:
        grade = "A"
    elif 80 <= percentage < 90:
        grade = "B"
    elif 70 <= percentage < 80:
        grade = "C"
    elif 60 <= percentage < 70:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)

    if percentage >= 50:
        print("Result: pass")
    else:
        print("Result: fail")

