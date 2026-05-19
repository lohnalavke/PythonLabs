import tkinter as tk
from tkinter import ttk, filedialog, Menu, Listbox, END, MULTIPLE

def load_file(event=None):
    """Загружает содержимое текстового файла в Listbox."""
    filename = filedialog.askopenfilename()
    if filename:
        listbox.delete(0, END)
        # Явно указываем кодировку UTF-8
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                listbox.insert(END, line.strip())

def delete_selected(event=None):
    """Удаляет выбранные элементы из Listbox."""
    selected = listbox.curselection()
    if selected:
        for index in reversed(selected):
            listbox.delete(index)

def save_file(event=None):
    """Сохраняет содержимое Listbox в новый файл."""
    filename = filedialog.asksaveasfilename()
    if filename:
        # При сохранении тоже используем UTF-8
        with open(filename, 'w', encoding='utf-8') as f:
            lines = [listbox.get(i) for i in range(listbox.size())]
            f.write('\n'.join(lines) + '\n')

# ---------- Главное окно ----------
root = tk.Tk()
root.title('Работа со списком (задание 46)')

# ---------- Меню ----------
menubar = Menu(root)
root['menu'] = menubar

menu_file = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='Файл')
menu_file.add_command(label='Открыть', command=load_file)
menu_file.add_command(label='Сохранить', command=save_file)

menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_edit, label='Правка')
menu_edit.add_command(label='Удалить', command=delete_selected)

# ---------- Listbox + Scrollbar ----------
frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky='nsew')

listbox = Listbox(frame, width=60, height=15, selectmode=MULTIPLE)
listbox.grid(column=0, row=0)

scrollbar = ttk.Scrollbar(frame, orient='vertical', command=listbox.yview)
scrollbar.grid(column=1, row=0, sticky='ns')
listbox.configure(yscrollcommand=scrollbar.set)

# ---------- Кнопки ----------
btn_frame = ttk.Frame(root)
btn_frame.grid(column=1, row=0, sticky='n')

ttk.Button(btn_frame, text='Открыть', command=load_file).pack(pady=2)
ttk.Button(btn_frame, text='Удалить', command=delete_selected).pack(pady=2)
ttk.Button(btn_frame, text='Сохранить', command=save_file).pack(pady=2)

root.mainloop()