import random
from art import logo
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def is_blackjack(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return True
    else:
        return False


def check_blackjack(user_cards, computer_cards):
    if is_blackjack(user_cards):
        print("You've got BLACKJACK!🤠")
        user_win()
    elif is_blackjack(computer_cards):
        print("Dealer got BLACKJACK!😡")
        user_loose()


def score_over_21(cards):
    return sum(cards) > 21


def get_user_score():
    return sum(user_cards)


def get_computer_score():
    return sum(computer_cards)


def user_win():
    print("You WIN!")


def user_loose():
    print("You LOOSE!")


user_cards = []
computer_cards = []

# deal initial hands
for n in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = get_user_score()
computer_score = get_computer_score()

check_blackjack(user_cards, computer_cards)

while True:

    user_score = get_user_score()
    computer_score = get_computer_score()

    if score_over_21(user_cards):
        user_cards = [1 if item == 11 else item for item in user_cards]
        user_score = get_user_score()
        if score_over_21(user_cards):
            user_loose()

    clear()
    print("User:")
    print(user_score)
    print(user_cards)
    print("\nComputer:")
    print(computer_score)
    print(computer_cards)

    draw_another_card = input("Do you want to draw another card? Type [y/n]: ")

    if draw_another_card.lower() == "y":
        user_cards.append(deal_card())
    else:
        break

while get_computer_score() < 17:
    computer_cards.append(deal_card())
    if score_over_21(computer_cards):
        user_win()

print(f"User score:\t{get_user_score()}\tCards:{user_cards}")
print(f"Computer score:\t{get_computer_score()}\tCards:{computer_cards}")

if get_user_score() > get_computer_score():
    user_win()
elif get_user_score() < get_computer_score():
    user_loose()
else:
    print("DRAW!")
