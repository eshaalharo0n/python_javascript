<<<<<<< HEAD
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
=======
import random


words = ["cat", "dog", "sun", "ball", "fish", "cake", "star", "tree"]


secret_word = random.choice(words)


chances = 6

guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", chances, "chances. Good luck!")


while chances > 0:

    
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "
    print("\nWord: ", display)

    
    all_guessed = True
    for letter in secret_word:
        if letter not in guessed_letters:
            all_guessed = False
    if all_guessed:
        print("You WIN! The word was:", secret_word)
        break

    
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one!")
        continue


    guessed_letters.append(guess)

    
    if guess in secret_word:
        print("Good job! That letter is in the word.")
    else:
        chances = chances - 1
        print("Oops! Wrong letter. Chances left:", chances)


if chances == 0:
    print("\nGame Over! The word was:", secret_word)
>>>>>>> eda9ce3 (assignemt python)
