#A school wants to automate the process of calculating student results.

#Write a program in Python that takes a student's information and generates a result card showing the total marks, percentage, grade, and pass/fail status.

name = input("enter your name :")
sub1 = int(input("enter your first subject number b/w 0 and 100 :"))
sub2 = int(input("enter you second number b/w 0 and 100 :"))
sub3 = int(input("enter your third subject number b/w 0 and 100 :"))
sub4 = int(input("enter your fourth subject number b/w 0 and 100 :"))
sub5 = int(input("enter your first subject number b/w 0 and 100 :"))
if not (0 <= sub1 <= 100 and
        0 <= sub2 <= 100 and
        0 <= sub3 <= 100 and
        0 <= sub4 <= 100 and
        0 <= sub5 <= 100):
    print("Invalid marks! All marks must be between 0 and 100.")
else:
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 500 * 100
print("student name :",name)
print("total marks :" , total ,"/500")
print("percentage",percentage,"%")
if 90 <= percentage <= 100:
    print("Grade: A")
elif 80 <= percentage < 90:
    print("Grade: B")
elif 70 <= percentage < 80:
    print("Grade: C")
elif 60 <= percentage < 70:
    print("Grade: D")
elif percentage <60 :
    print("Grade: F")    
else:
    print("invalid")                

if 50<=percentage< 60 :
    print("Result: fail")
else :
    print("Result: pass")    