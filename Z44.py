import tkinter as tk
from tkinter import ttk
import random

#Увеличение и уменьшение на 1
def plus_one(event):
    current = int(num.get())
    num.set(str(current + 1))

def minus_one(event):
    current = int(num.get())
    num.set(str(current - 1))

prog = tk.Tk()
prog.title('Счётчик')

num = tk.StringVar(value='0')
entry = ttk.Entry(textvariable=num, width=10)
entry.grid(column=0, row=0, columnspan=2)

btn_plus = ttk.Button(text='+1')
btn_plus.bind('<Button-1>', plus_one)
btn_plus.grid(column=0, row=1)

btn_minus = ttk.Button(text='-1')
btn_minus.bind('<Button-1>', minus_one)
btn_minus.grid(column=1, row=1)

prog.mainloop()

#Увеличение и уменьшения в полях(пункт 2)
def change(amount):
    current = float(num1.get())
    num1.set(str(current + amount))

def add(event):
    change(float(num2.get()))

def sub(event):
    change(-float(num2.get()))

prog = tk.Tk()
prog.title('Изменение на величину')

num1 = tk.StringVar(value='0')
num2 = tk.StringVar(value='1')

ttk.Label(text='Число:').grid(column=0, row=0, sticky='w')
entry1 = ttk.Entry(textvariable=num1, width=10)
entry1.grid(column=1, row=0)

ttk.Label(text='Шаг:').grid(column=0, row=1, sticky='w')
entry2 = ttk.Entry(textvariable=num2, width=10)
entry2.grid(column=1, row=1)

btn_add = ttk.Button(text='+')
btn_add.bind('<Button-1>', add)
btn_add.grid(column=0, row=2)

btn_sub = ttk.Button(text='-')
btn_sub.bind('<Button-1>', sub)
btn_sub.grid(column=1, row=2)

prog.mainloop()

# Пункт 3(сумма трех случайных чисел)
def calc_sum(event):
    a = float(num1.get())
    b = float(num2.get())
    c = float(num3.get())
    result.set(str(a + b + c))

prog = tk.Tk()
prog.title('Сумма трёх чисел')

# Случайные начальные значения от 1 до 10
num1 = tk.StringVar(value=str(random.randint(1, 10)))
num2 = tk.StringVar(value=str(random.randint(1, 10)))
num3 = tk.StringVar(value=str(random.randint(1, 10)))
result = tk.StringVar(value='')

ttk.Label(text='Число 1:').grid(column=0, row=0, sticky='w')
ttk.Entry(textvariable=num1, width=10).grid(column=1, row=0)

ttk.Label(text='Число 2:').grid(column=0, row=1, sticky='w')
ttk.Entry(textvariable=num2, width=10).grid(column=1, row=1)

ttk.Label(text='Число 3:').grid(column=0, row=2, sticky='w')
ttk.Entry(textvariable=num3, width=10).grid(column=1, row=2)

ttk.Label(text='Сумма:').grid(column=0, row=3, sticky='w')
ttk.Entry(textvariable=result, width=10).grid(column=1, row=3)

btn = ttk.Button(text='Вычислить')
btn.bind('<Button-1>', calc_sum)
btn.grid(column=0, row=4, columnspan=2)

prog.mainloop()

#Пункт 4(накопление суммы)

def add_to_total(event):
    a = float(num1.get())
    b = float(num2.get())
    c = float(num3.get())
    current = float(total.get()) if total.get() else 0.0
    total.set(str(current + a + b + c))

prog = tk.Tk()
prog.title('Накопление суммы')

num1 = tk.StringVar(value=str(random.randint(1, 10)))
num2 = tk.StringVar(value=str(random.randint(1, 10)))
num3 = tk.StringVar(value=str(random.randint(1, 10)))
total = tk.StringVar(value='0')

ttk.Label(text='Число 1:').grid(column=0, row=0, sticky='w')
ttk.Entry(textvariable=num1, width=10).grid(column=1, row=0)

ttk.Label(text='Число 2:').grid(column=0, row=1, sticky='w')
ttk.Entry(textvariable=num2, width=10).grid(column=1, row=1)

ttk.Label(text='Число 3:').grid(column=0, row=2, sticky='w')
ttk.Entry(textvariable=num3, width=10).grid(column=1, row=2)

ttk.Label(text='Общая сумма:').grid(column=0, row=3, sticky='w')
ttk.Entry(textvariable=total, width=10).grid(column=1, row=3)

btn = ttk.Button(text='Прибавить сумму')
btn.bind('<Button-1>', add_to_total)
btn.grid(column=0, row=4, columnspan=2)

prog.mainloop()