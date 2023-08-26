#----------------------------------------------------
# Tk-enter?
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def chenge_theme(theme):
    text_fild['bg'] = viem_coors[theme]['text_bg']
    text_fild['fg'] = viem_coors[theme]['text_fg']
    text_fild['insertbackground'] = viem_coors[theme]['cursor']
    text_fild['selectbackground'] = viem_coors[theme]['select_bg']
    

def chenge_fonts(fontss):
    text_fild['font'] = fonts[fontss]['font']
    
def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы действительно желаете выйти.')
    if answer:
        root.destroy()

def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        text_fild.delete("1.0", END)
        text_fild.insert("1.0", open(file_path, encoding='utf-8').read())
        
def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()

root = Tk()
root.title("Текстовый редактор.")
root.geometry('600x700')
root.iconbitmap('icon.ico')

main_menu = Menu(root)
root.config(menu=main_menu)

# файл.
fiel_menu = Menu(main_menu, tearoff=0)
fiel_menu.add_command(label="Открыть", command=open_file)
fiel_menu.add_command(label="Сохранить", command=save_file)
fiel_menu.add_separator()
fiel_menu.add_command(label="Закрыть", command=notepad_exit)
root.config(menu=fiel_menu)

# Вид и темы.
viem_menu = Menu(main_menu, tearoff=0)
viem_menu_sub = Menu(viem_menu, tearoff=0)
font_manu_sub = Menu(viem_menu, tearoff=0)

viem_menu_sub.add_command(label="Темная тема", command=lambda:chenge_theme('dark'))
viem_menu_sub.add_command(label="Светлая тема", command=lambda:chenge_theme('light'))
viem_menu.add_cascade(label='Тема', menu=viem_menu_sub)

font_manu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_manu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))
font_manu_sub.add_command(label='Times Nem Roman', command=lambda: chenge_fonts('TNR'))
viem_menu.add_cascade(label='Шрифты', menu=font_manu_sub)
root.config(menu=viem_menu)



# Добавление списков меню.
main_menu.add_cascade(label="Файл", menu=fiel_menu)
main_menu.add_cascade(label="Вид", menu=viem_menu)

root.config(menu=main_menu)

#-------------------------------------------------------------------------------------------------------------
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

viem_coors = {
    'dark':{
        'text_bg':'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg':'#F4A460'
    },
    
    'light':{
        'text_bg':'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg':'#FAEEDD'
    }
}


fonts = {
    'Arial':{
        'font':'Arial 10 bold'
    },
    
    'CSMS':{
        'font': ('Comic Sans MS', 10, 'bold')
    },
    
    'TNR':{
        'font': ('Times Nem Roman', 10, 'bold')
    }
}

text_fild = Text(f_text,
                bg='black',
                fg='lime', padx=10,
                pady=10,
                wrap=WORD,
                insertbackground="#B00000",
                selectbackground="#F4A460",
                spacing3=10,
                width=30,
                font='Arial 10 bold',
                )
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)


root.mainloop()