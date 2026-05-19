import tkinter as tk
from tkinter import ttk, colorchooser

# ---------- Глобальные переменные ----------
current_color = 'black'
current_width = 2
lastx, lasty = None, None
lines = []               # id нарисованных линий

# ---------- Класс для кнопок цвета ----------
class ColorButton(ttk.Button):
    """Кнопка, меняющая цвет рисования при нажатии."""
    def __init__(self, color, **kwargs):
        super().__init__(text=color, **kwargs)   # только text, не color
        self.color = color
        self.bind('<Button-1>', self.set_color)

    def set_color(self, event):
        global current_color
        current_color = self.color

# ---------- Рисование ----------
def save_posn(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def add_line(event):
    global lastx, lasty, lines
    line_id = canvas.create_line(lastx, lasty, event.x, event.y,
                                 fill=current_color, width=current_width)
    lines.append(line_id)
    lastx, lasty = event.x, event.y

# ---------- Управление ----------
def choose_color():
    global current_color
    _, color_tuple = colorchooser.askcolor(initialcolor=current_color)
    if color_tuple:
        current_color = color_tuple

def set_width(event=None):
    global current_width
    try:
        w = int(width_var.get())
        if w > 0:
            current_width = w
    except ValueError:
        pass

def clear_canvas():
    global lines
    canvas.delete('all')
    lines = []

def undo_last():
    global lines
    if lines:
        last_id = lines.pop()
        canvas.delete(last_id)

# ---------- Окно и холст ----------
root = tk.Tk()
root.title('Графический редактор (задание 47)')

canvas = tk.Canvas(root, width=500, height=400, background='white')
canvas.grid(column=0, row=0, rowspan=10, columnspan=2)

canvas.bind('<Button-1>', save_posn)
canvas.bind('<B1-Motion>', add_line)

# ---------- Элементы управления ----------
# Толщина
ttk.Label(root, text='Толщина:').grid(column=2, row=0, sticky='w')
width_var = tk.StringVar(value=str(current_width))
width_entry = ttk.Entry(root, textvariable=width_var, width=5)
width_entry.grid(column=3, row=0)
width_entry.bind('<Return>', set_width)
ttk.Button(root, text='Установить', command=set_width).grid(column=4, row=0)

# Кнопки стандартных цветов (используем класс ColorButton)
colors = ['black', 'red', 'green', 'blue', 'orange', 'purple']
for i, col in enumerate(colors):
    ColorButton(col).grid(column=2 + i % 2, row=1 + i // 2, sticky='we')

# Кнопка вызова диалога цвета
ttk.Button(root, text='Другой цвет...', command=choose_color).grid(
    column=2, row=4, columnspan=2, sticky='we')

# Кнопка отмены
ttk.Button(root, text='Отменить', command=undo_last).grid(
    column=2, row=5, columnspan=2, sticky='we')

# Кнопка очистки
ttk.Button(root, text='Очистить', command=clear_canvas).grid(
    column=2, row=6, columnspan=2, sticky='we')

root.mainloop()