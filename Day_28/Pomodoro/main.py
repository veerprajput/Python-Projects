from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
first_stage = '✔'
second_stage = '✔✔'
third_stage = '✔✔✔'
fourth_stage = '✔✔✔✔'
reps2 = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    global reps2
    global timer
    window.after_cancel(timer)
    label['text'] = 'Timer:'
    canvas.itemconfig(t, text='00:00')
    reps = 0
    reps2 = 0
    check_marks['text'] = ''

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
    global reps
    global reps2
    work_sec = round(WORK_MIN * 60)
    short_break_sec = round(SHORT_BREAK_MIN * 60)
    long_break_sec = round(LONG_BREAK_MIN * 60)
    
    reps += 1
    
    if reps % 2 == 1:
        count_down(work_sec)
        label['text'] = 'Work'
    elif reps == 8:
        count_down(long_break_sec)
        label['text'] = 'Long Break'
        reps2 += 1
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label['text'] = 'Short Break'
        reps2 += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    global reps2
    count_minute = math.floor(count / 60)
    count_second = count % 60
    
    # if reps2 % 2 == 0:
    if reps2 == 1:
        check_marks['text'] = first_stage
    elif reps2 == 2:
        check_marks['text'] = second_stage
    elif reps2 == 3:
        check_marks['text'] = third_stage
    elif reps2 == 4:
        check_marks['text'] = fourth_stage
    
    if count_second < 10:
        count_second = f'0{count_second}'
    
    canvas.itemconfig(t, text=f'{count_minute}:{count_second}')
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(bg=YELLOW, padx=200, pady=200)

label = Label(fg=GREEN, text='Timer', bg=YELLOW, font=(FONT_NAME, 50))
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
t = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.config(bg=YELLOW)
canvas.grid(row=1, column=1)

button1 = Button(text='Start', highlightthickness=0, command=start)
button1.grid(row=2, column=0)

button2 = Button(text='Reset', highlightthickness=0, command=reset)
button2.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=32)
check_marks.grid(column=1, row=3)

window.mainloop()