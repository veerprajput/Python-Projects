from tkinter import *
import random
import pandas as pd

try:
    csv_data = pd.read_csv('words_to_learn.csv')
except FileNotFoundError:
    csv_data = pd.read_csv('frenchwords.csv')
d = csv_data.to_dict(orient='records')
card = {}

def pick():
    global card, ft
    window.after_cancel(ft)
    canvas.itemconfig(image, image=card_img)
    canvas.itemconfig(title, text='French', fill='black')
    card = random.choice(d)
    canvas.itemconfig(word, text=card['French'], fill='black')
    ft = window.after(3000, func=nc)

def pick_for_check():
    global card, ft
    d.remove(card)
    window.after_cancel(ft)
    canvas.itemconfig(image, image=card_img)
    canvas.itemconfig(title, text='French', fill='black')
    card = random.choice(d)
    canvas.itemconfig(word, text=card['French'], fill='black')
    ft = window.after(3000, func=nc)

def nc():
    global card
    canvas.itemconfig(word, text=card['English'], fill='white')
    canvas.itemconfig(image, image=back_img)
    canvas.itemconfig(title, text='English', fill='white')

def check():
    pass

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

ft = window.after(3000, func=nc)

canvas = Canvas(width=890, height=576, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = PhotoImage(file='images/card_front.png')
image = canvas.create_image((450, 288), image=card_img)
title = canvas.create_text((450, 170), text="French", font=('Arial', 40, 'italic'))
word = canvas.create_text((450, 270), text="trouve", font=('Arial', 60, 'bold'))
canvas.grid(row=1, column=0, columnspan=2)
back_img = PhotoImage(file='images/card_back.png')

w_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=w_img, highlightthickness=0, command=pick)
wrong_button.grid(row=2, column=0)

c_img = PhotoImage(file='images/right.png')
correct_button = Button(image=c_img, highlightthickness=0, command=pick_for_check)
correct_button.grid(row=2, column=1)

pick()

window.mainloop()

dd = pd.DataFrame(d)

dd.to_csv('words_to_learn.csv', index=False)
