from prettytable import PrettyTable, DOUBLE_BORDER
from util import clear

from data import words
from art import logo
import random


CORRECT_WORD = random.choice(words).upper()
print("Clue: " + CORRECT_WORD)

table = PrettyTable()
table.set_style(DOUBLE_BORDER)
TABLE_HEADER = ["⚔", "W", "Ö", "R", "D", "L", "E"]

table.field_names = TABLE_HEADER
clear()
print(logo)
print("Clue: " + CORRECT_WORD)
print(table)


MAX_ATTEMPTS = 6
WORD_LENGTH = 6
attempt = 1


def is_valid_word(word, length):
    return len(word) == length and word.isalpha()


def user_guess():
    while True:
        guess = input("Enter a word: ").strip().upper()
        if is_valid_word(guess, WORD_LENGTH):
            return guess
        else:
            print(f"Invalid word! Make sure the word is {WORD_LENGTH} letters long")


def format(word, CORRECT_WORD, attempt):
    formatted_answer = []
    attempt_number = [f"{attempt}."]
    formatted_answer.extend(attempt_number)

    word_list = [char for char in word]

    for char in range(len(word_list)):
        if word_list[char] == CORRECT_WORD[char]:
            word_list[char] = f"[{word_list[char]}]"
        elif word_list[char] in CORRECT_WORD:
            word_list[char] = f"({word_list[char]})"

    formatted_answer.extend(word_list)

    return formatted_answer


def update_table(formatted_answer):
    table.add_row(formatted_answer)


def update_board():
    clear()
    print(logo)
    print(table)


while attempt <= MAX_ATTEMPTS:
    answer = user_guess()
    formatted_answer = format(answer, CORRECT_WORD, attempt)
    update_table(formatted_answer)
    update_board()

    if answer != CORRECT_WORD and attempt == MAX_ATTEMPTS:
        print(f"You lost! The correct word was: {CORRECT_WORD}")
        break
    elif answer == CORRECT_WORD:
        print("You won")
        break
    else:
        print("Wrong. Try again.")

    attempt += 1


# x Randomly select a 6 letter word, this is the correct word
# x Attempts = 6
#   (Nice to have: Choose attempts)


# x Ask for word from user
# x Word should only contains letters, exactly 'len' letters in length
# x if word break rules, ask for new word

# Print playboard
