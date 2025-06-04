# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas

npa = pandas.read_csv('nato_phonetic_alphabet.csv')


letters = npa.letter.to_list()
codes = npa.code.to_list()

letters_and_values = {letters[letter]:codes[letter] for letter in range(len(letters))}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generator():
    ntcw = input('Enter a word that you want to convert: ').upper()

    try:
        nato_words = [letters_and_values[letter] for letter in ntcw]
    except:
        print('Sorry letters only')
        generator()

    try:
        print(nato_words)
    except:
        pass

generator()