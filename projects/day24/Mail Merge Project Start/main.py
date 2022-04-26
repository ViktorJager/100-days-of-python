PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_template = letter_file.readlines()

with open("./Input/Names/invited_names.txt") as name_file:
    invited_names = name_file.readlines()
    for name_index in range(len(invited_names)):
        invited_names[name_index] = invited_names[name_index].strip('\n')


for name in invited_names:
    custom_letter = letter_template.copy()
    custom_letter[0] = custom_letter[0].replace(PLACEHOLDER, name)

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as complete_letter:
        for row in custom_letter:
            complete_letter.write(row)

