import os
import time

import tkinter.filedialog, tkinter as tk, time

from tkinter import *
from tkinter import messagebox as mb, filedialog

def app_exit():
    answer = tkinter.messagebox.askokcancel(u'Выход', u'Вы точно хотите выйти из РусОфис Word?')
    if answer:
        app.destroy()


def change_theme(theme):
    textbox['bg'] = view_colors[theme]['text_bg']
    textbox['fg'] = view_colors[theme]['text_fg']


def change_fonts(fontsg):
    global fontText
    textbox['font'] = fonts[fontsg]['font']
    fontText = textbox['font']

def NewWindow():
    os.system("start RusOffice.exe")

def NewFile():
    answer = tkinter.messagebox.askokcancel(u'Создание нового файла', u'Вы точно хотите создать новый файл? Весь несохраненный контент будет удален!')
    if answer:
        textbox.delete('1.0', 'end')
        textbox.pack()
        app.title('РусОфис 1.0')

def info():
    tkinter.messagebox.showinfo('РусОфис', 'РусОфис 1.0.0 \n Программа для чтения и записи текстовых файлов \n Cherni Company, 2024')

def LoadFile():
    global cur_path
    try:
        ftypes = [
        (u'Все файлы', '*'), (u'Текстовые файлы', '*.txt'), (u'Python код', '*.py'), (u'C++ код', '*.cpp'), (u'Разметка HTML', '*.html'), (u'Разметка CSS', '*.css'), (u'RusOffice Word', '*.row'),]
        fn = tkinter.filedialog.Open(app, filetypes=ftypes).show()
        if fn == '':
            return
        textbox.delete('1.0', 'end')
        textbox.insert('1.0', open(fn, encoding='utf-8').read())
        cur_path = fn
        app.title(f'РусОфис 1.0 - {cur_path}')
    except UnicodeDecodeError:
        tkinter.messagebox.showerror('Ошибка кодирования', 'Во время открытия файла произошла ошибка кодирования в "UTF-8"!')

def SaveFile():
    SaveFile = open(cur_path, "w", encoding='utf-8')
    text = textbox.get('1.0', END)
    SaveFile.write(text)
    SaveFile.close()

def SaveAllFile():
    file_path = filedialog.asksaveasfilename(defaultextension='.*', filetypes=((u'Все файлы', '*'), (u'Текстовые файлы', '*.txt'), (u'Python код', '*.py'), (u'C++ код', '*.cpp'), (u'Разметка HTML', '*.html'), (u'Разметка CSS', '*.css'), (u'RusOffice Word', '*.row')))
    f = open(file_path, 'w', encoding='utf-8')
    text = textbox.get('1.0', END)
    f.write(text)
    f.close()

def LeftJu():
    textbox.tag_configure('filled', justify='left')
    textbox.tag_add('filled','1.0','end')

def CenterJu():
    textbox.tag_configure('filled', justify='center')
    textbox.tag_add('filled','1.0','end')

def RightJu():
    textbox.tag_configure('filled', justify='right')
    textbox.tag_add('filled','1.0','end')

def close_file():
    answer = tkinter.messagebox.askokcancel(u'Закрытие файла', u'Вы точно хотите закрыть файл? Весь несохраненный контент будет удален!')
    if answer:
        textbox.delete('1.0', 'end')
        textbox.pack()
        app.title('РусОфис 1.0')

class App(tk.Tk):
    def __init__(self):
        super().__init__()

sizeText = 11

app = App()
app.iconbitmap('icon.ico')
app.geometry('1366x768')
app.state('zoomed')
app.title('РусОфис 1.0')
textFrame = Frame(app, height=340, width=600)
textFrame.pack(side='bottom', fill='both', expand=1) 
textbox = Text(textFrame, font='Colibri 11', wrap=WORD)
scrollbar = Scrollbar(textFrame)
scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')
menu = tk.Menu()
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label=u'Создать', command=NewFile)
file_menu.add_command(label=u'Открыть', command=LoadFile)
file_menu.add_command(label=u'Новое окно', command=NewWindow)
file_menu.add_separator()
file_menu.add_command(label=u'Сохранить', command=SaveFile)
file_menu.add_command(label=u'Сохранить как', command=SaveAllFile)
file_menu.add_separator()
file_menu.add_command(label=u'Закрыть файл', command=close_file)
file_menu.add_command(label=u'Выход', command=app_exit)
menu.add_cascade(label=u'Файл', menu=file_menu)
view_menu = Menu(menu, tearoff=0)

menu.add_cascade(label=u'Фон и текст', menu=view_menu)
view_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label=u'Светлый', command=(lambda : change_theme('light')))
view_menu_sub.add_command(label=u'Темный', command=(lambda : change_theme('dark')))
view_menu.add_cascade(label=u'Фон', menu=view_menu_sub)

font_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub.add_command(label='Times New Roman', command=(lambda : change_fonts('Times New Roman')))
font_menu_sub.add_command(label='Comic Sans MS', command=(lambda : change_fonts('CSMS')))
font_menu_sub.add_command(label='Colibri', command=(lambda : change_fonts('Colibri')))
font_menu_sub.add_command(label='Arial', command=(lambda : change_fonts('Arial')))
view_menu.add_cascade(label=u'Шрифты', menu=font_menu_sub)

'''fontSize_menu_sub = Menu(view_menu, tearoff=0)
fontSize_menu_sub.add_command(label='11px', command=(change_sizeText(11)))
fontSize_menu_sub.add_command(label='14px', command=(change_sizeText(14)))
fontSize_menu_sub.add_command(label='18px', command=(change_sizeText(18)))
fontSize_menu_sub.add_command(label='20px', command=(change_sizeText(20)))
fontSize_menu_sub.add_command(label='24px', command=(change_sizeText(24)))
fontSize_menu_sub.add_command(label='36px', command=(change_sizeText(36)))
fontSize_menu_sub.add_command(label='48px', command=(change_sizeText(48)))
fontSize_menu_sub.add_command(label='72px', command=(change_sizeText(72)))
view_menu.add_cascade(label=u'Размер шрифта', menu=fontSize_menu_sub)
'''
urov_menu_sub = Menu(view_menu, tearoff=0)
urov_menu_sub.add_command(label='Влево', command=(LeftJu))
urov_menu_sub.add_command(label='По центру', command=(CenterJu))
urov_menu_sub.add_command(label='Вправо', command=(RightJu))
view_menu.add_cascade(label=u'Уравнивание текста', menu=urov_menu_sub)

font = textbox['font']

view_colors = {'dark':{'text_bg':'gray4', 
  'text_fg':'white'}, 
  'light':{'text_bg':'white', 
  'text_fg':'black'}}

fonts = {'Times New Roman':{'font': ('Times New Roman', sizeText)}, 
 'CSMS':{'font': ('Comic Sans MS', sizeText)}, 
 'Colibri':{'font': ('Colibri', sizeText)}, 
 'Arial':{'font': ('Arial', sizeText)}}

menu.add_command(label=u'О программе', command=info)
menu.add_command(label=u'Выход', command=app_exit)
app.config(menu=menu)
app.bind('<Control-s>', lambda e: SaveFile())
app.bind('<Control-q>', lambda e: SaveAllFile())
app.bind('<Control-o>', lambda e: LoadFile())
app.bind('<Control-w>', lambda e: close_file())
app.bind('<Control-e>', lambda e: CenterJu())
app.bind('<Control-l>', lambda e: LeftJu())
app.bind('<Control-r>', lambda e: RightJu())
app.bind('<Alt-F4>', lambda e: app_exit())
app.mainloop()
