import random
from art import logo
from misc import clear


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Randomly pick the correct number
correct_number = random.randint(1, 101)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {correct_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Set the player attempts
player_attempts = (
    EASY_LEVEL_TURNS if difficulty == "e" or difficulty == "easy" else HARD_LEVEL_TURNS
)

# Game loop variable
game_over = False

while not game_over:

    clear()
    print(logo)

    # Display player attempts left
    print(f"You have {player_attempts} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))

    if player_guess == correct_number:
        game_over = True
    elif player_guess > correct_number:
        print("Too high!")
    elif player_guess < correct_number:
        print("Too low!")

    player_attempts -= 1
    if player_attempts == 0:
        game_over = True


if player_guess == correct_number:
    print("You WIN!")
else:
    print("You've run out of guesses, you LOOSE!")
