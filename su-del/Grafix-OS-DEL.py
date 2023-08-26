# Начало приветствие
from tkinter import *
import tkinter as tk
import time
import pyglet
from tkinter import messagebox
from tkinter import filedialog

print("       Starting OS")
time.sleep(1)
print("       Loading")
time.sleep(0.5)

time.sleep(1)
print("\n       Grafix OS.del v/1.0 \n ")

# Выбор компонента или решения

time.sleep(1)
print("\n          Для запуска OS введите 'start-OS'  ")
time.sleep(1)
print("\n          Для полной устоновки OS введите 'update-OS'  ")
time.sleep(1)
print("\n          Для обновления OS введите 'upgrade-OS' \n ")
time.sleep(1)
print("\n          Полный вход в систему 'start-upgrade.OS' \n")
time.sleep(1)
print("\n          Выход и отключение 'exit' \n ")

# Выполнение решения или компонента

while True:
    commandel = input(" 0?/: \n >>>  ")
    if commandel == "start-OS":
        time.sleep(0.1)
        print("\n       Загрузка...  ")
        time.sleep(0.1)
        print("\n       Подключение к сети Del.sys...  ")
        time.sleep(0.1)
        print("\n       Успешно. \n ")
        time.sleep(0.1)
        print("\n       Для входа введите 'Users-OS'. \n ")
        
    if commandel == "start-upgrade.OS":
        time.sleep(1)
        print ("    [Проверка обновлений [Обновления...]]")
        import time
        import sys
        toolbar_width = 40
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))
        for i in range(toolbar_width):
            time.sleep(0.5)
            sys.stdout.write("-")
            sys.stdout.flush()
        sys.stdout.write("]\n")
        print("\n")
        print("Обновление загружено и установлено в систему")
        time.sleep(1)
        print("\n       Загрузка...  ")
        time.sleep(10.5)
        print("\n       Подключение к сети Del.sys...  ")
        time.sleep(5.8)
        print("\n       Успешно. \n ")
        time.sleep(5.8)
        print("\n       Для входа введите 'Users-del'. \n ")
        
    if commandel == "update-OS":
        time.sleep(1)
        print("\n       Загрузка...  ")
        print ("    [Активация файлов.]")
        import time
        import sys
        toolbar_width = 40
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))
        for i in range(toolbar_width):
            time.sleep(1.0)
            sys.stdout.write("-")
            sys.stdout.flush()
        sys.stdout.write("]\n")
        
        print ("    [Распаковка файловой системы.]")
        import time
        import sys
        toolbar_width = 40
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))
        for i in range(toolbar_width):
            time.sleep(1.5)
            sys.stdout.write("-")
            sys.stdout.flush()
        sys.stdout.write("]\n")
        
        print ("    [Завершение и проверка обновлений.]")
        import time
        import sys
        toolbar_width = 40
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))
        for i in range(toolbar_width):
            time.sleep(0.5)
            sys.stdout.write(">")
            sys.stdout.flush()
        sys.stdout.write("]\n")
        print("\n")
        
    if commandel == "upgrade-OS":
        time.sleep(1)
        print("\n       Загрузка...  ")
        print ("    [Обновление системмы.]")
        import time
        import sys
        toolbar_width = 40
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))
        for i in range(toolbar_width):
            time.sleep(0.3)
            sys.stdout.write("-")
            sys.stdout.flush()
        sys.stdout.write("]\n")
        print("\n")
        
    if commandel == "exit":
            print("выход")
            break
        
    if commandel == "Users-OS":
        time.sleep(1)
        print("\n           Загрузка...  \n")
        print("             Вход выполнен успешно. \n")
        print("             Используйте 'help' для подключения к графическому интерфейсу.")
        print("             Используйте 'info' для отображения информации о сборке.")
        print("             Для запуска виртуальной машини введите 'START'")
        
        
# Вход в системму выполнен успешно OS/del      

  
        while True:
            commandel = input(" OS.DEL?/: \n >>>  ")
            if commandel == "info":
                print("\n")
                print("       Используйте 'help' для подключения к графическому интерфейсу.")
                print("       Используйте 'info' для отображения информации о сборке.")
                print("       Для запуска виртуальной машини введите 'START'")
                print("       Deliex.del, OS-del, System.osgrafix.del")
                print("       Version 1.0.0")
                print("       Activation code: \n       [ERROR-4665] \n")
                
            if commandel == "help":
                print("\n")
                print("       Grafix.del       (Вход в графический интерфейс.)")
                print("       Выход из Del     (Переход в начальный католог (0?/:).)")
                print("\n")
                
            if commandel == "Выход из Del":
                print("Вы перейдёте в начальный католог (0?/:)")
                break
            
            if commandel == "START":
                print("Вы перейдёте в графический режим через консоль.")
                print("Введите код доступа, для входа в систему.")
                
# Grafix.del  
                while True:
                    command1i = input(" OS.DEL?/User/del-user/control/sys: ")
                    if command1i == "1708":
                        print("\n")
                        time.sleep(1)
                        print("Запуск оконого режима.")
                        print("\n")
                        time.sleep(1)
                        from tkinter import *
                        import tkinter as tk
                        import time
                        import pyglet
                
                        tk = Tk()
                        tk.title("Virtual.del/OS.DEL")
                        tk.resizable(False, False)
                        canvas = Canvas(tk, width=1366, height=768)
                        canvas.pack()
                        logo1 = PhotoImage(file="logo.png")
                        canvas.create_image(0,0,anchor=NW,image=logo1)
                        startmusic1 = pyglet.resource.media("startmusic.mp3")
                        startmusic1.play()
                        tk.update()
                        tk.after(3000) # 3.sec
                        desktop1 = PhotoImage(file="desktop.png")
                        canvas.create_image(0,0,anchor=NW,image=desktop1)
                        
                        #images Начало
                        picture1 = PhotoImage(file="picture1.png")
                        
                        #click button окно
                        def button_press():
                            #playmus1.place_forget()
                            canvas.create_image(0,0,anchor=NW, image=desktop1)
                            
                            from FILESPROG import messagebox, time, tkintermapview, tkinter
                        
                    #button окно
                        win1 = Button(tk, text="Мой диск", background="blue", foreground="black", command= button_press)
                        win1.place(x=10, y=10, width=100,height=50)
                        
                    #click button Блокнот
                        def button_press():
                            #playmus1.place_forget()
                            canvas.create_image(0,0,anchor=NW, image=desktop1)
                            
                            #----------------------------------------------------
                            # Tk-enter?
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

                            root = Toplevel()
                            root.title("Текстовый редактор.")
                            root.geometry('600x700')
                            root.grab_set()
                            #root.overrideredirect(1)
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
                            
                    #button Блокнот
                        win1 = Button(tk, text="Блокнот", background="blue", foreground="black", command= button_press)
                        win1.place(x=120, y=10, width=100,height=50)
