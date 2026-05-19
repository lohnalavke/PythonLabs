import tkinter as tk
from tkinter import ttk

# ---------- Глобальные переменные ----------
hidden = 0      # память (предыдущее значение)
preoper = ''    # предыдущая операция

# ---------- Класс для цифровых кнопок ----------
class DButton(ttk.Button):
    def __init__(self, symbol):
        super().__init__(text=symbol)
        self.symbol = symbol
        self.bind('<Button-1>', self.renov)

    def renov(self, event):
        stext.set(stext.get() + self.symbol)

# ---------- Класс для кнопок операций ----------
class OButton(ttk.Button):
    def __init__(self, symbol):
        super().__init__(text=symbol)
        self.symbol = symbol
        self.bind('<Button-1>', self.oper)

    def oper(self, event):
        global hidden, preoper
        if hidden != 0:
            if preoper == '+':
                hidden += float(stext.get())
            elif preoper == '-':
                hidden -= float(stext.get())
            elif preoper == '*':
                hidden *= float(stext.get())
            elif preoper == '/':
                hidden /= float(stext.get())
        else:
            hidden = float(stext.get())

        if self.symbol in ('=', 'C'):
            if self.symbol == '=':
                stext.set(str(hidden))
            else:
                stext.set('')
            preoper = ''
            hidden = 0
        else:
            stext.set('')
            preoper = self.symbol

# ---------- Создание главного окна ----------
prog = tk.Tk()
prog.title('Калькулятор')

# Текстовое поле
stext = tk.StringVar(value='')
entry = ttk.Entry(textvariable=stext, width=30)
entry.grid(column=0, row=0, columnspan=4)

# Координаты для цифр и точки
coords_digits = [(0,1), (1,1), (2,1),
                 (0,2), (1,2), (2,2),
                 (0,3), (1,3), (2,3),
                 (1,4), (2,4)]   # 1..9, 0, .
digits = '1234567890.'

for sym, coord in zip(digits, coords_digits):
    btn = DButton(sym)
    btn.grid(column=coord[0], row=coord[1])

# Координаты для кнопок операций
coords_ops = [(3,1), (3,2), (3,3), (3,4), (4,1), (4,4)]  # +, -, *, /, C, =
ops = '+-*/C='

for sym, coord in zip(ops, coords_ops):
    btn = OButton(sym)
    btn.grid(column=coord[0], row=coord[1])

# Кнопка смены знака
def change_sign(event):
    s = stext.get()
    if s.startswith('-'):
        stext.set(s[1:])
    else:
        stext.set('-' + s)

btn_sign = ttk.Button(text='-/+')
btn_sign.bind('<Button-1>', change_sign)
btn_sign.grid(column=0, row=4)

# Кнопка удаления последнего символа
def backspace(event):
    stext.set(stext.get()[:-1])

btn_back = ttk.Button(text='<-')
btn_back.bind('<Button-1>', backspace)
btn_back.grid(column=4, row=2)

prog.mainloop()