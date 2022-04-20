from data import words

def generate_wordlist(len):
    word_dict = words
    word_arr = []

    for w in word_dict:
        if len(w) == len:
            word_arr.append(w)

    print(word_arr)

