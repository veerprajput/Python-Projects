#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from tkinter.font import names


x = 1
# name = input('What is your name: ')
names = []

with open('Input/Letters/starting_letter.txt') as file:
    for line in file.readlines():
        line.strip()
        with open('Input/Names/invited_names.txt') as file2:
            for line2 in file2:
                names.append(line2)
        
        # for name in names:
            # for num in range(1, 4):
        if x == 1:
            print(f'{line[0:4]} {line[5:11].replace(line[5:11], names[0])} {line[12:]}')
            x += 1
        elif line == 'Dear [name],':
            print(None)
        else:
            print(line)
