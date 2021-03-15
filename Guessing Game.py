# This is a "guess the number" game

import random

print("Hello! What is your name?")
name = input()

print("Hello " + name + ", I am thinking of a number between 1 and 20, can you guess what it is?")
randomNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print("Take a guess")
    guessedNumber = int(input())

    if guessedNumber < randomNumber:
        print("Sorry! your guess is too low")
    elif guessedNumber > randomNumber:
        print("Oops! your guess is too high")
    else:
        break


if guessedNumber == randomNumber:
    print("CONGRATULATIONS! YOU HAVE GUESSED THE SECRET NUMBER!")
    print("And you have guessed the number in " + str(guessesTaken) + " guesses.")
else:
    print("Nope~ The number I was thinking of is " + str(randomNumber) + ".")


