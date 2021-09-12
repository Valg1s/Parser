from tkinter import *
from tkinter import messagebox
from main import for_GUI

root = Tk()


def btn_click():
    URL = URLInput.get()
    #print(URL)
    pages = pagesInput.get()
    info_str = for_GUI(pages, URL)
    # info_str = f'Data: {str(URL)}'
    messagebox.showinfo(title='Name', message=info_str)
    


root['bg'] = '#fafafa'
root.title('Parser')
root.wm_attributes('-alpha', 1)
root.geometry('500x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=500, width=250)
canvas.pack()

frame = Frame(root, bg='#a1f6ff')
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

title = Label(root, text='Парсинг Auto ria', bg='white', font='Times 25')
title.place(height=40, width=250, x=125, y=20)
btn = Button(frame, text='Запуск', bg='yellow', command=btn_click, font='Times 12')
btn.place(height=30, width=100, x=180, y=65)

title_URLInput = Label(frame, text='Ссылка на машины', font='Times 25')
title_URLInput.place(height=40, width=280, x=50, y=110)

URLInput = Entry(frame, bg='white', font='Times 15', justify='center')
URLInput.place(height=40, width=280, x=50, y=160)

title_pagesInput = Label(frame, text='Кол-во\nстраниц', font='Times 10')
title_pagesInput.place(height=40, width=50, x=350, y=110)

pagesInput = Entry(frame, bg='white', font='Times 15', justify='center')
pagesInput.place(height=40, width=50, x=350, y=160)

root.mainloop()