import pandas as pd

word_user_enters = input('Enter a word that you want to convert: ').upper()
npa = pd.read_csv('Morse_code.csv')

letters, codes = npa.letter.to_list(), npa.code.to_list()
letters_and_values = {letters[letter]:codes[letter] for letter in range(len(letters))}

def generator():
    nato_words = [letters_and_values[letter] for letter in word_user_enters]
    for word in nato_words:
        print(word)
generator()