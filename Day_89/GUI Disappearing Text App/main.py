import tkinter

window = tkinter.Tk()
window.title('Disappearing Text App')
window.minsize(width=900, height=600)
window.configure(background="#ff6969")

def check_entry():
    if entry.get("1.0", "end-1c") == entry.old_value:
        entry.delete("1.0", "end")
    entry.old_value = entry.get("1.0", "end-1c")

label = tkinter.Label(text='Disappearing Text App', font=('Arial', 36, 'italic', 'bold'))
label.configure(background="#ff6969", foreground="#FFFFFF")
label.place(x=195, y=10)

entry = tkinter.Text(window, height=25, width=92,font=('Arial', 12))
entry.place(x=35, y=100)

entry.old_value = entry.get("1.0", "end-1c")

def update_entry():
    entry.old_value = entry.get("1.0", "end-1c")
    window.after(10000, check_entry)
    window.after(5000, update_entry)

update_entry()

window.mainloop()
