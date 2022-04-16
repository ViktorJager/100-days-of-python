import art
import random
from game_data import data
from misc import clear


def get_random_account():
    return random.choice(data)


def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def get_correct_answer(account_a, account_b):
    return "a" if account_a["follower_count"] > account_b["follower_count"] else "b"


# End game, present score and follower count
def end_of_game(acc_a, acc_b, player_score):
    print(f"\nSorry, that's wrong!")
    print(f"{acc_a['name']}: {acc_a['follower_count']} mil")
    print(f"{acc_b['name']}: {acc_b['follower_count']} mil")
    print(f"FINAL SCORE: {player_score}")


def game():
    player_score = 0
    account_a = get_random_account()
    account_b = get_random_account()

    while True:
        print(art.logo)
        print(f"Current score: {player_score}")

        # present compairson
        print(format_data(account_a))
        print(art.vs)
        print(format_data(account_b))

        # get player answer
        player_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct_answer = get_correct_answer(account_a, account_b)
        if player_answer == correct_answer:
            player_score += 1
            account_a = account_b
            account_b = get_random_account()
        else:
            end_of_game(account_a, account_b, player_score)
            break
        clear()


game()

while input("Play again? [y/n]") == "y":
    clear()
    game()
