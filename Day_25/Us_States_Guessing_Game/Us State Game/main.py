import pandas as pd
import turtle
import time

screen = turtle.Screen()
screen.title('U.S.A States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

csv_return_data = pd.read_csv('50_states.csv')

data = csv_return_data.to_dict()
more_data = csv_return_data['state'].to_list()
x_data = csv_return_data['x'].to_list()
y_data = csv_return_data['y'].to_list()
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
spell_checker = turtle.Turtle()
spell_checker.penup()
spell_checker.hideturtle()
screen.tracer(0)
states_guessed_already = []
states_guessed = 0

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title='Guess the State', prompt="What's another state's name").title()
    if answer_state == 'Exit':
        break
    spell_checker.goto(90, 270)
    spell_checker.color('dark orange')
    spell_checker.write(f'SCORE: {states_guessed}/50', font=('Courier', 20, 'normal'))
    for state in data['state']:
        if answer_state == more_data[state]:
            x = x_data[state]
            y = y_data[state]
            
            writer.goto(x, y)
            writer.write(f'{answer_state}')
            screen.update()
            
            
            if answer_state in states_guessed_already:
                pass
            else:
                states_guessed += 1
                states_guessed_already.append(answer_state)
            
            if states_guessed == 50:
                writer.goto(-140, 280)
                writer.color('black')
                writer.write('You win!!', font=('Courier', 32, 'bold'))
                spell_checker.clear()
                spell_checker.color('dark orange')
                spell_checker.write(f'SCORE: {states_guessed}/50', font=('Courier', 30, 'normal'))
                time.sleep(5)
                exit()
        if answer_state not in more_data:
            spell_checker.goto(-330, 50)
            spell_checker.color('red')
            spell_checker.write('Check the spelling again!!!', font=('Courier', 32, 'bold'))
            time.sleep(1)
            spell_checker.goto(90, 270)
            spell_checker.clear()
            spell_checker.color('dark orange')
            spell_checker.write(f'SCORE: {states_guessed}/50', font=('Courier', 30, 'normal'))
            answer_state = screen.textinput(title='Guess the State', prompt="What's another state's name").title()
    
    spell_checker.goto(90, 270)
    spell_checker.clear()
    spell_checker.color('dark orange')
    spell_checker.write(f'SCORE: {states_guessed}/50', font=('Courier', 30, 'normal'))
    # answer_state = screen.textinput(title='Guess the State', prompt="What's another state's name").title()

ngs = [more_data[state] for state in data['state'] if more_data[state] not in states_guessed_already]
# for state in data['state']:
#     if more_data[state] not in states_guessed_already:
#         ngs.append(more_data[state])

stl = pd.DataFrame(ngs)
stl.to_csv('states_to_learn.csv')