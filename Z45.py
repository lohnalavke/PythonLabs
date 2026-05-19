# пункт 1
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def write_fio(event):
    #Записывает ФИО в файл ФИО.txt на дозапись
    fio = name.get() + ' ' + patr.get() + ' ' + surn.get()
    with open('ФИО.txt', 'a', encoding='utf-8') as f:
        f.write(fio + '\n')

prog = Tk()
prog.title('Запись ФИО')

# Метки
ttk.Label(text='Имя:').grid(column=0, row=0, sticky='w')
ttk.Label(text='Отчество:').grid(column=0, row=1, sticky='w')
ttk.Label(text='Фамилия:').grid(column=0, row=2, sticky='w')

# Поля ввода (изначально пустые)
name = StringVar(value='')
patr = StringVar(value='')
surn = StringVar(value='')

ttk.Entry(textvariable=name).grid(column=1, row=0)
ttk.Entry(textvariable=patr).grid(column=1, row=1)
ttk.Entry(textvariable=surn).grid(column=1, row=2)

# Кнопка записи
btn = ttk.Button(text='Записать')
btn.bind('<Button-1>', write_fio)
btn.grid(column=0, row=3, columnspan=2)

prog.mainloop()

# пункт 2

def write_fio_dialog(event):
    #Открывает диалог сохранения и дописывает ФИО с категорией
    fname = filedialog.asksaveasfilename()
    if fname:   # если пользователь не отменил диалог
        fio = name.get() + ' ' + patr.get() + ' ' + surn.get()
        line = fio + ' ' + age.get()
        with open(fname, 'a', encoding='utf-8') as f:
            f.write(line + '\n')

prog = Tk()
prog.title('Запись ФИО с возрастом')

# Метки и поля ввода
ttk.Label(text='Имя:').grid(column=0, row=0, sticky='w')
ttk.Label(text='Отчество:').grid(column=0, row=1, sticky='w')
ttk.Label(text='Фамилия:').grid(column=0, row=2, sticky='w')

name = StringVar(value='')
patr = StringVar(value='')
surn = StringVar(value='')

ttk.Entry(textvariable=name).grid(column=1, row=0)
ttk.Entry(textvariable=patr).grid(column=1, row=1)
ttk.Entry(textvariable=surn).grid(column=1, row=2)

# Радиокнопки для возрастной категории
age = StringVar(value='ребёнок')   # значение по умолчанию
categories = ['ребёнок', 'подросток', 'взрослый', 'пенсионер', 'умер']

ttk.Label(text='Возраст:').grid(column=0, row=3, sticky='w')
for i, cat in enumerate(categories):
    rb = ttk.Radiobutton(text=cat, variable=age, value=cat)
    rb.grid(column=1, row=3+i, sticky='w')

# Кнопка записи с диалогом
btn = ttk.Button(text='Записать в файл')
btn.bind('<Button-1>', write_fio_dialog)
btn.grid(column=0, row=8, columnspan=2)

prog.mainloop()