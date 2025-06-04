from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
gp = ''

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password():
    global gp
    global letters
    global numbers
    global symbols
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    input3.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def search():
    true = False
    try:
        with open('data.json', 'r') as passwords:
            data = json.load(passwords)
            for k,v in data.items():
                website = input1.get()
                if website == k:
                    can_be_saved = messagebox.showinfo(title=website,
                    message=f"Your email for this website is {v['email']}\nYour password for this website is {v['password']}")
                    true = True
            if true == False:
                messagebox.showinfo(title='ERROR', message='That website does not exist in my database')
    except:
        messagebox.showinfo(title='Error', message='File could not be found')
                

def sp():
    website = input1.get()
    login = input2.get()
    password = input3.get()
    can_be_saved = None
    new_data = {
        website: {
                'email': login,
                'password': password,

            },
        }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="You left some fields empty", message="Error, You left some fields empty\n Check again")
    else:
        can_be_saved = messagebox.askokcancel(title=website, message='Are you sure you want to save this')

        if can_be_saved:
            try:
                with open('data.json', 'r') as passwords:
                    data = json.load(passwords)
                    data.update(new_data)

                with open('data.json', 'w') as passwords:
                    json.dump(data, passwords, indent=4)
            except:
                with open('data.json', 'w') as passwords:
                    json.dump(new_data, passwords, indent=4)

            finally:# passwords.write('\n')
                input1.delete(0, END)
                input3.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image((100, 100), image=lock_img)
canvas.grid(row=0, column=1)

label = Label(highlightthickness=0, text='Website: ')
label.grid(row=1, column=0)
label2 = Label(highlightthickness=0, text='Email/Username: ')
label2.grid(row=2, column=0)
label3 = Label(highlightthickness=0, text='Password: ')
label3.grid(row=3, column=0)

input1 = Entry(highlightthickness=0, width=31)
input1.grid(row=1, column=1)
input1.focus()
input2 = Entry(highlightthickness=0, width=50)
input2.grid(row=2, column=1, columnspan=2)
input2.insert(0, 'learner@gmail.com')
input3 = Entry(width=31)
input3.grid(row=3, column=1)

button1 = Button(text='Generate Password', command=password)
button1.grid(row=3, column=2)
button2 = Button(width=42, text='Add', command=sp)
button2.grid(row=4, column=1, columnspan=2)
button3 = Button(text='Search', width=13, command=search)
button3.grid(row=1, column=2)

window.mainloop()

