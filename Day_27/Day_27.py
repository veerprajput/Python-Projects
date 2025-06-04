from tkinter import *

window = Tk()
window.title('GUI')
window.minsize(width=800, height=500)
window['bg'] = 'cyan'

label = Label(text='asjdl;faskdjfl;asdfj;', font=('Courier', 24, 'italic'))
label.pack()

def bl():
    label['text'] = input.get()

button = Button(text='Click Me', command=bl)
button.pack()

input = Entry(width=20)
input.insert(END, string='Enter some text? ')
input.pack()

def s():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=s )
spinbox.pack

window.mainloop()
