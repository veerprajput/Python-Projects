print('''
      |  |
    --------
      |  |
    --------
      |  |
      ''')
print('Welcome to Tic Tac Toe')

import random

numbers_user_guessed = []
numbers_computer_guessed = []
numbers_computor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def last_main():
    if 1 in numbers_user_guessed and  2 in numbers_user_guessed and 3 in numbers_user_guessed:
        print('You Win')
    elif 1 in numbers_computer_guessed and  2 in numbers_computer_guessed and 3 in numbers_computer_guessed:
        print('You lose')
    elif 4 in numbers_user_guessed and 5 in numbers_user_guessed and 6 in numbers_user_guessed:
        print('You Win')
    elif 4 in numbers_computer_guessed and 5 in numbers_computer_guessed and 6 in numbers_computer_guessed:
        print('You lose')
    elif 7 in numbers_user_guessed and  8 in numbers_user_guessed and 9 in numbers_user_guessed:
        print('You Win')
    elif 7 in numbers_computer_guessed and  8 in numbers_computer_guessed and 9 in numbers_computer_guessed:
        print('You lose')
    elif 1 in numbers_user_guessed and  5 in numbers_user_guessed and 9 in numbers_user_guessed:
        print('You Win')
    elif 1 in numbers_computer_guessed and  5 in numbers_computer_guessed and 9 in numbers_computer_guessed:
        print('You lose')
    elif 3 in numbers_user_guessed and  5 in numbers_user_guessed and 7 in numbers_user_guessed:
        print('You Win')
    elif 3 in numbers_computer_guessed and  5 in numbers_computer_guessed and 7 in numbers_computer_guessed:
        print('You lose')
    else:
        print('TIE')

def take_input():
    tic_tac_toe_input = int(input(f'Enter a number from these numbers {numbers_computor}? '))
    if tic_tac_toe_input > 9:
        print('Greator than 9')
        tic_tac_toe_input = int(input('Enter a number from one to nine? '))
    numbers_computor.remove(tic_tac_toe_input)
    computer_input = random.choice(numbers_computor)
    print(computer_input)
    numbers_computor.remove(computer_input)
    numbers_user_guessed.append(tic_tac_toe_input)
    numbers_computer_guessed.append(computer_input)
take_input()
take_input()
take_input()
last_main()


