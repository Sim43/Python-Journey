import random

import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Type a difficulty. Type 'easy' or 'hard': ")
target = random.randint(1, 100)

if difficulty == "easy":
    lives = 10
else:
    lives = 5

isFinished = False
while lives != 0 and not isFinished:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == target:
        print(f"You got it! The answer was {target}")
        isFinished = True
    elif guess > target:
        print("Too high.\nGuess again.")
        lives -= 1
    else:
        print("Too low.\nGuess again.")
        lives -= 1
if lives == 0:
    print("You've run out of gasses, you lose.")
