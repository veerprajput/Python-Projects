#κάκτος
import time
import tkinter
import threading
import random
started=False
num=0
high_wpm = 0

def timer():
    global started
    global num
    while started:
        time.sleep(0.1)
        num += 0.1
        wps = len(typing_entry.get().split()) / num
        wpm = wps * 60
        high_wpm = wpm
        cps = len(typing_entry.get()) / num
        cpm = cps * 60
        typing_speed.config(text=f'{round(cps,2)} CPS\n {round(cpm,2)} CPM\n{round(wps,2)} WPS\n{round(wpm,2)} WPM\n{highscore} WPM Highscore')


def start(event):
    global started
    global num
    global wpm
    global highscore
    if not started:
        if not event.keycode in [16, 17, 18]:
            started = True
            t = threading.Thread(target=timer)
            t.start()
    if label.cget('text')[:-1] == typing_entry.get():
        started = False
        if float(highscore) < high_wpm:
            open('highscore.txt', 'w').write(str(high_wpm))

window = tkinter.Tk()
window.title('Typing Speed Test')
window.geometry('900x600')
texts = open('text.txt', 'r').read().split('\n')
label = tkinter.Label(window, text=random.choice(texts), font=('Arial', 20))
label.grid(row=0, column=0, columnspan=2)
highscore = open('highscore.txt', 'r').read()
typing_entry = tkinter.Entry(window, width=40, font=('Arial', 25))
typing_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
typing_entry.bind('<KeyPress>', start)
typing_speed = tkinter.Label(window, text=f'0.00 CPS\n 0.00 CPM\n0.00 WPS\n 0.00 WPM\n{highscore} WPM Highscore')
typing_speed.grid(row=2, column=0, columnspan=2)
window.mainloop()


# import time
# import tkinter
# import threading
# import random
# started=False
# num=0

# def time_thread():
#     global started
#     global num
#     while started:
#         time.sleep(0.1)
#         num += 0.1
#         wps = len(typing_entry.get().split()) / num
#         wpm = wps * 60
#         cps = len(typing_entry.get()) / num
#         cpm = cps * 60
#         typing_speed.config(text=f'{round(cps,2)} CPS\n {round(cpm,2)} CPM\n{round(wps,2)} WPS\n{round(wpm,2)} WPM')

# def start(event):
#     global started
#     global num
#     if not started:
#         if not event.keycode in [16, 17, 18]:
#             started = True
#             t = threading.Thread(target=time_thread)
#             t.start()
#     if not label.cget('text') == typing_entry.get():
#         typing_entry.config(fg='red')
#     if label.cget('text')[:-1] == typing_entry.get():
#         started = False
#         typing_entry.config(fg='green')
            





# window = tkinter.Tk()
# window.title('Typing Speed Test')
# window.geometry('900x600')
# texts = open('text.txt', 'r').read().split('\n')
# frame = tkinter.Frame(window)
# label = tkinter.Label(frame, text=random.choice(texts), font=('Arial', 20))
# label.grid(row=0, column=0, columnspan=2, pady=10)
# typing_entry = tkinter.Entry(frame, width=40, font=('Arial', 25))
# typing_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
# typing_entry.bind('<KeyPress>', start)
# typing_speed = tkinter.Label(frame, text='0.00 CPS\n 0.00 CPM\n0.00 WPS\n 0.00 WPM')
# typing_speed.grid(row=2, column=0, columnspan=2)
# frame.pack(expand=True)
# # window.after(1, timer)

# window.mainloop()
