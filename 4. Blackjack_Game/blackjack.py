import random
import clear
import art


def deal_card():
    cards = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return random.choice(cards)


def add_cards(cards):
    result = 0
    for card in cards:
        if card == 'J' or card == 'Q' or card == 'K':
            card = '10'
        if card != 'A':
            result += int(card)
        else:
            if result + 11 > 21:
                result += 1
            else:
                result += 11
    return result


def highest_check(player_cards, computer_cards):
    if len(computer_cards) == 1:
        return
    if add_cards(player_cards) > 21 and add_cards(computer_cards) > 21:
        print(f"Your final hand: {player_cards}\nComputer's final hand: {computer_cards}\nYou Lost!")
    elif add_cards(player_cards) > 21:
        print(f"Your final hand: {player_cards}\nComputer's final hand: {computer_cards}\nYou went over. Your Lose.")
    elif add_cards(computer_cards) > 21:
        print(f"Your final hand: {player_cards}\nComputer's final hand: {computer_cards}\nComputer went over. Your Win.")
    elif add_cards(player_cards) == add_cards(computer_cards):
        print(f"Your final hand: {player_cards}\nComputer's final hand: {computer_cards}\nIt's a Draw!")
    elif add_cards(player_cards) == 21:
        print(f"Your final hand: {player_cards}\nComputer's final hand: {computer_cards}\nWin with a Blackjack.")
    elif add_cards(computer_cards) == 21:
        print(f"Your final hand: {player_cards}\nComputer's final hand: {computer_cards}\nLose, opponent has Blackjack.")
    elif add_cards(player_cards) > add_cards(computer_cards):
        print(f"Your final hand: {player_cards}\nComputer's final hand: {computer_cards}\nYou Won!")
    else:
        print(f"Your final hand: {player_cards}\nComputer's final hand: {computer_cards}\nYou Lost!")


def recursive_play():
    clear.clear()
    print(art.logo)
    hit = 'y'
    is_finished = False
    yorn = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if yorn == 'y':
        player_cards = [deal_card(), deal_card()]
        print(f"Your cards: {player_cards}")
        computer_cards = [deal_card(), deal_card()]
        print(f"Computer's first card: {computer_cards[0]}")
        highest_check(player_cards, computer_cards[0])
        while hit == 'y' and not is_finished:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == 'y':
                player_cards.append(deal_card())
                if add_cards(player_cards) >= 21:
                    while add_cards(computer_cards) < 17:
                        computer_cards.append(deal_card())
                    highest_check(player_cards, computer_cards)
                    is_finished = True
                else:
                    print(f"Your hand: {player_cards}\nComputer's first card: {computer_cards[0]}")
            else:
                while add_cards(computer_cards) < 17:
                    computer_cards.append(deal_card())
                highest_check(player_cards, computer_cards)
                is_finished = True
        recursive_play()
    else:
        return


recursive_play()
print("Goodbye!")
