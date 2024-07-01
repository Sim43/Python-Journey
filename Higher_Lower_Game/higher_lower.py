import clear

import game_data

import art

import random


def compare(a, b, our_choice):
    if our_choice == 'A':
        if a['follower_count'] >= b['follower_count']:
            return True
        else:
            return False
    else:
        if b['follower_count'] >= a['follower_count']:
            return True
        else:
            return False


def play():
    data = game_data.data
    choice_a = random.choice(data)
    choice_b = random.choice(data)
    global score
    while choice_a == choice_b:
        choice_b = random.choice(data)
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print(art.vs)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
    player_choice = input("Who has more followers? Type 'A' or 'B': ")
    player_choice.upper()
    if compare(choice_a, choice_b, player_choice):
        score += 1
        clear.clear()
        print(art.logo)
        print(f"You're right! Current score: {score}")
        play()
    else:
        clear.clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        return


print(art.logo)
score = 0
play()
