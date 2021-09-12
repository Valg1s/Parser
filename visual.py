from tkinter import *
from tkinter import messagebox

root = Tk()


def btn_click():
    URL = URLInput.get()
    print(URL)
    # info_str = f'Data: {str(URL)}'
    # messagebox.showinfo(title='Name', message=info_str)
    


root['bg'] = '#fafafa'
root.title('Parser')
root.wm_attributes('-alpha', 1)
root.geometry('500x180')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=500, width=180)
canvas.pack()

frame = Frame(root, bg='blue')
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

title = Label(root, text='Парсинг Auto ria', bg='white', font='Times 25')
title.place(height=40, width=250, x=125, y=20)
btn = Button(frame, text='Запуск', bg='yellow', command=btn_click, font='Times 15')
btn.place(height=30, width=100, x=180, y=65)

URLInput = Entry(frame, bg='white')
URLInput.place(height=40, width=350, x=50, y=110)

root.mainloop()