student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


import pandas

# student_data_frame = pandas.DataFrame("nato_phonetic_alphabet")
student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {}


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    phonetic_dict[row.letter] = row.code
    # Access index and row
    # Access row.student or row.score
# ALTERNATIVE:
# phonetic_dict = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What do you want to translate? ").upper()

translation = [phonetic_dict[letter] for letter in user_input]
print(translation)
