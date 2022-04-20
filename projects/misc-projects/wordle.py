from prettytable import PrettyTable, DOUBLE_BORDER
from util import clear

from data import words
import random



searched_word = random.choice(words).upper()
print(searched_word)

table = PrettyTable()
table.set_style(DOUBLE_BORDER)
TABLE_HEADER = ["⚔", "W", "O", "R", "D", "L", "E"]

table.field_names = TABLE_HEADER
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
            print ("That was not an acceptable word.")
    
def format(word, attempt):
    formatted_answer = []

    attempt_number = [f"{attempt}."]
    word_list = [char for char in word]

    formatted_answer.extend(attempt_number)
    formatted_answer.extend(word_list)

    return formatted_answer

def update_table(answer):
    table.add_row(formatted_answer)
    print(table)


while attempt <= MAX_ATTEMPTS:

    answer = user_guess()
    formatted_answer = format(answer, attempt)
    update_table(formatted_answer)

    if answer != searched_word and attempt == MAX_ATTEMPTS:
        print("You lost!")
        break
    elif answer == searched_word:
        print("You won")
        break
    else:
        print("Wrong. Try again.")

    attempt += 1
    




''' rows = [ [ " " ] * 7 ] * 5
answer_as_list = list(answer)
rows[0] = answer_as_list '''



""" table.field_names = ["⚔", "W", "O", "R", "D", "L", "E"]

for row in rows: 
    table.add_rows(
        [
            row
        ]
    ) 

print(table)  """



def wrap_char(type, char):
    match type:
        case "parenthesis":
            return f"({char})"
        case "bracket":
            return f"[{char}]"
        case "space" | _:
            return f" {char} "


# x Randomly select a 6 letter word, this is the correct word
# Attempts = 6


# Ask for word from user
# Word should only contains letters, exactly 6 letters in length
# if word break rules, ask for new word

# Print playboard

