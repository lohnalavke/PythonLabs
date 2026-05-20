import tkinter as tk
from tkinter import ttk
import numpy as np

# ---------- Функции ----------
def calculate(event=None):
    """Вычисляет недостающий параметр по двум известным."""
    # Множители единиц
    if Henry.get() == 'нГн':
        multH = 1e-9
    elif Henry.get() == 'мкГн':
        multH = 1e-6
    elif Henry.get() == 'мГн':
        multH = 1e-3
    else:
        multH = 1.0   # если вдруг не выбрано

    if Farad.get() == 'пФ':
        multF = 1e-12
    elif Farad.get() == 'нФ':
        multF = 1e-9
    elif Farad.get() == 'мкФ':
        multF = 1e-6
    else:
        multF = 1.0

    if Hertz.get() == 'Гц':
        multHz = 1
    elif Hertz.get() == 'кГц':
        multHz = 1e3
    elif Hertz.get() == 'МГц':
        multHz = 1e6
    else:
        multHz = 1.0

    # Получаем значения из полей
    L_val = L_entry.get()
    C_val = C_entry.get()
    f_val = f_entry.get()

    # Определяем, какое поле пустое, и вычисляем
    if L_val == '' and C_val != '' and f_val != '':
        C = float(C_val) * multF
        f = float(f_val) * multHz
        L = 1 / (4 * np.pi**2 * f**2 * C)
        L_entry.delete(0, tk.END)
        L_entry.insert(0, str(L / multH))
    elif C_val == '' and L_val != '' and f_val != '':
        L = float(L_val) * multH
        f = float(f_val) * multHz
        C = 1 / (4 * np.pi**2 * f**2 * L)
        C_entry.delete(0, tk.END)
        C_entry.insert(0, str(C / multF))
    elif f_val == '' and L_val != '' and C_val != '':
        L = float(L_val) * multH
        C = float(C_val) * multF
        f = 1 / (2 * np.pi * np.sqrt(L * C))
        f_entry.delete(0, tk.END)
        f_entry.insert(0, str(f / multHz))

def clear_all(event=None):
    """Очищает все поля ввода."""
    L_entry.delete(0, tk.END)
    C_entry.delete(0, tk.END)
    f_entry.delete(0, tk.END)

# ---------- Окно приложения ----------
root = tk.Tk()
root.title('Калькулятор колебательного LC-контура')

# ---------- Холст с рисунком контура ----------
canvas = tk.Canvas(root, width=500, height=200)
canvas.grid(column=0, row=0, columnspan=3, pady=10)

# Рисуем схематичный LC-контур (как в учебнике)
canvas.create_line(150, 20, 350, 20, width=2)
canvas.create_line(150, 180, 350, 180, width=2)
canvas.create_line(120, 90, 180, 90, width=2)
canvas.create_line(120, 100, 180, 100, width=2)
canvas.create_line(150, 20, 150, 90, width=2)
canvas.create_line(150, 100, 150, 180, width=2)
canvas.create_line(350, 20, 350, 40, width=2)
canvas.create_line(350, 160, 350, 180, width=2)
canvas.create_arc(335, 40, 365, 70, start=90, extent=-180, width=2, style=tk.ARC)
canvas.create_arc(335, 70, 365, 100, start=90, extent=-180, width=2, style=tk.ARC)
canvas.create_arc(335, 100, 365, 130, start=90, extent=-180, width=2, style=tk.ARC)
canvas.create_arc(335, 130, 365, 160, start=90, extent=-180, width=2, style=tk.ARC)

# ---------- Параметры ----------
# Индуктивность
ttk.Label(root, text='Индуктивность L', font='Arial 14').grid(
    column=0, row=1, padx=10, pady=10, sticky='w')
L_entry = ttk.Entry(root, font='Arial 14', width=10)
L_entry.grid(column=1, row=1, padx=10, pady=10)

Henry = tk.StringVar(value='мГн')
varHenry = ttk.Combobox(root, textvariable=Henry, values=('нГн', 'мкГн', 'мГн'),
                        font='Arial 14', width=8)
varHenry.grid(column=2, row=1, padx=10, pady=10)
varHenry.current(2)   # по умолчанию мГн

# Ёмкость
ttk.Label(root, text='Ёмкость C', font='Arial 14').grid(
    column=0, row=2, padx=10, pady=10, sticky='w')
C_entry = ttk.Entry(root, font='Arial 14', width=10)
C_entry.grid(column=1, row=2, padx=10, pady=10)

Farad = tk.StringVar(value='мкФ')
varFarad = ttk.Combobox(root, textvariable=Farad, values=('пФ', 'нФ', 'мкФ'),
                        font='Arial 14', width=8)
varFarad.grid(column=2, row=2, padx=10, pady=10)
varFarad.current(2)

# Частота
ttk.Label(root, text='Частота f', font='Arial 14').grid(
    column=0, row=3, padx=10, pady=10, sticky='w')
f_entry = ttk.Entry(root, font='Arial 14', width=10)
f_entry.grid(column=1, row=3, padx=10, pady=10)

Hertz = tk.StringVar(value='кГц')
varHertz = ttk.Combobox(root, textvariable=Hertz, values=('Гц', 'кГц', 'МГц'),
                        font='Arial 14', width=8)
varHertz.grid(column=2, row=3, padx=10, pady=10)
varHertz.current(1)

# ---------- Кнопки ----------
ttk.Button(root, text='Рассчитать', command=calculate).grid(
    column=1, row=4, pady=10)
ttk.Button(root, text='Очистить', command=clear_all).grid(
    column=2, row=4, pady=10)

root.mainloop()