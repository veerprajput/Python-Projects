import random
import hangman_words


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = hangman_words.word_list
word = random.choice(word_list)
word_length = len(word)



print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

display = []
for _ in range(word_length):
    display += "_"
    

lives = 6



while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    
    if guess in display:
      print(f"you've already guessed {guess}")

    for position in range(word_length):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    if guess not in word:
      lives -= 1
      print(f"Your letter {guess} was not in that word. You lose a life")
      print(stages[lives])
      if lives == 0:
        print('You lose')
        break
        

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
        break

print(word)