from tkinter import *

window = Tk()
window.title('GUI')
window.minsize(width=900, height=500)
# window['bg'] = 'cyan'

def calculate():
    label3['text'] = round(int(input1.get()) * 1.6, 1)

i = Label(width=30)
i.grid(column=0, row=0)

input1 = Entry(width=30, font=('Bold', 32, 'normal'))
input1.grid(column=1, row=0)

label1 = Label(width=10, text='Miles', font=('Bold', 32, 'normal'))
label1.grid(column=2, row=0)

label2 = Label(width=10, text='is equal to', font=('Bold', 32, 'normal'))
label2.grid(column=1, row=1)

label3 = Label(width=10, text=0, font=('Bold', 32, 'normal'), fg='blue', bg='cyan')
label3.grid(column=1, row=2)

label4 = Label(width=10, text='Km', font=('Bold', 32, 'normal'), fg='blue', bg='cyan')
label4.grid(column=2, row=2)

button1 = Button(width=10, text='Calculate', command=calculate, font=('Bold', 32, 'normal'))
button1.grid(column=1, row=3)

label5 = Label(width=39, text='''*Use: Enter the number in the box,
            to convert from MI to KMs
            and press "calculate" button.''', font=('Courier', 17, 'italic'))
label5.config(padx=0, pady=450)
label5.grid(column=0, row=4)


window.mainloop()