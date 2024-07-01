import random
import clear
import hangman_art
import hangman_words


def print_display(blanks):
    for letter in blanks:
        print(letter, end=" ")
    print("\n")


print(hangman_art.logo)
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
stages = hangman_art.stages
lives = 6
display = ["_"] * len(chosen_word)
print(chosen_word)
print_display(display)
while display.count("_") != 0 and lives != 0:
    guess = input("Guess: ")
    guess.lower()
    clear.clear()
    for n in range(0, len(chosen_word)):
        if chosen_word[n] == guess:
            display[n] = guess
    if chosen_word.count(guess) == 0:
        lives -= 1
        print(f"You guessed {guess}, that's not int the word. You loose a life.")
    print(stages[lives])
    print_display(display)
    if lives == 0:
        print("You've lost.")
print("You've won.")