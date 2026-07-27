import random

words = ["python", "computer", "programming", "keyboard", "internet"]

word = random.choice(words)

guessed = []
wrong = 0
chances = 6

print(" Welcome to Hangman!")

while wrong < chances:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)
    print("Wrong guesses:", wrong, "/", chances)

    if display == word:
        print(" You Win!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed this letter!")
    elif guess in word:
        print("Correct guess!")
        guessed.append(guess)
    else:
        print(" Wrong guess!")
        guessed.append(guess)
        wrong += 1

if wrong == chances:
    print(" You Lost!")
    print("The word was:", word)