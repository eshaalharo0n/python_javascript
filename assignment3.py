###Create a program in python that asks the user to enter 5 numbers.

def check_number(number):
    if number % 2 == 0:
        print("Even")
        return "even"
    else:
        print("Odd")
        return "odd"

even_count = 0
odd_count = 0

for i in range(5):
    num = int(input("Enter number: "))
    result = check_number(num)

    if result == "even":
        even_count += 1
    else:
        odd_count += 1

print("Total Even Numbers:", even_count)
print("Total Odd Numbers:", odd_count)
        



