from tkinter import *
import tkinter as tk
import time
import pyglet
from tkinter import messagebox
from tkinter import filedialog

#----------------------------------------------------
#Tk-enter?
del1 = Tk()
del1.title("Файлы")
del1.geometry('600x400')
del1.grab_set()
#del1.overrideredirect(1)
del1.resizable(width=False, height=False) 
del1.iconbitmap('icon.ico')

#----------------------------------------------------

#++===================================================================================================================++

#clik Btn C?
def сustor():
    del12 = Toplevel()
    del12.title("FILES C?/ ")
    del12.geometry('600x400')
    del12.grab_set()
    #del12.overrideredirect(1)
    del12.resizable(width=False, height=False)
    del12.iconbitmap('icon.ico')
    
    # Games
    
    # Крестики нолики 
    
    #btn click games
    def russr():
        
        def russr():
            import maing

            
            
        btn120 = Button(del12,
                text="Крестики нолики?/ >",
                command=russr,
                font ='Arial 8 bold',
                #Цвет основы кнопки
                bg='#BF930D',
                #Цвет при нажатии
                activebackground = 'lime',
                #Цвет букв в кнопкке
                activeforeground = '#480607',
                fg="#480607"
                )
        btn120.grid(column=1, row=2)
    
    #btn games
    btn12 = Button(del12,
                text="GAMES?/ >",
                command=сustorm,
                font ='Arial 8 bold',
                #Цвет основы кнопки
                bg='#BF930D',
                #Цвет при нажатии
                activebackground = 'lime',
                #Цвет букв в кнопкке
                activeforeground = '#480607',
                fg="#480607"
                )
    btn12.grid(column=1, row=2)

#++===================================================================================================================++

#Btn C?
btn1 = Button(del1,
                text="C?/ >",
                command=сustor,
                font ='Arial 8 bold',
                bg='lime',
                activebackground = 'red',
                activeforeground = 'lime',
                fg="#480607"
                )
btn1.grid(column=1, row=2)

#----------------------------------------------------
#clik Btn DEL?
def delus():
    lbl2 = Label(del1, text="Доступно. /DEL: ")
    lbl2.grid(column=0, row=2)

#Btn DEL?
btn2 = Button(del1,
            text="DEL?/ >",
            command=delus,
            font ='Arial 8 bold',
            bg='lime',
            activebackground = 'red',
            activeforeground = 'lime',
            fg="#480607"
            )
btn2.grid(column=3, row=0)

#----------------------------------------------------
#clik Btn ROOT?
def rootus():
    lbl = Label(del1, text="Заблокировано /ROOT: ")
    lbl.grid(column=0, row=3)

#Btn ROOT?
btn3 = Button(del1,
            text="ROOT?/ >",
            command= rootus,
            font ='Arial 8 bold',
            bg='red',
            activebackground = 'red',
            activeforeground = 'lime',
            fg="#480607"
            )
btn3.grid(column=4, row=0)

#----------------------------------------------------

del1.mainloop()