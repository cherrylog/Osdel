from tkinter import *
from tkinter import messagebox
import time
#import tkintermapview
# Файловый менеджер 1
#----------------------------------------------------
#Tk-enter?

del1 = Tk()
del1.title("FILESPROG.DEL")
del1.geometry('610x30')
del1.resizable(width=False, height=False)

#----------------------------------------------------

#----------------------------------------------------
#clik Btn DEOS?
def сus():
    from DEOS import tqdm, time
#Btn C?
btn1 = Button(del1,
            text="DEOS?/ >",
            command=сus,
            font ='Arial 8 bold',
            bg='lime',
            activebackground = 'red',
            activeforeground = 'lime',
            fg="#480607"
            )
btn1.grid(column=1, row=0)

#----------------------------------------------------

#----------------------------------------------------
#clik Btn Змейка?
def delus():
    from Shakgame import turtle, random
    

#Btn Змейка?
btn2 = Button(del1,
            text="Змейка?/ >",
            command=delus,
            font ='Arial 8 bold',
            bg='lime',
            activebackground = 'red',
            activeforeground = 'lime',
            fg="#480607"
            )
btn2.grid(column=2, row=0)

#----------------------------------------------------

#----------------------------------------------------
#clik Btn Блокнот?
def textru():
    from textfile import messagebox, filedialog

#Btn Блокнот?
btn3 = Button(del1,
            text="Блокнот?/ >",
            command= textru,
            font ='Arial 8 bold',
            bg='lime',
            activebackground = 'red',
            activeforeground = 'lime',
            fg="#480607"
            )
btn3.grid(column=3, row=0)

#----------------------------------------------------

#----------------------------------------------------
#clik Btn YADER?
def YADER():
    from Yader import time

#Btn Блокнот?
btn4 = Button(del1,
            text="YADER.DEL?/ >",
            command= YADER,
            font ='Arial 8 bold',
            bg='lime',
            activebackground = 'red',
            activeforeground = 'lime',
            fg="#480607"
            )
btn4.grid(column=4, row=0)

#----------------------------------------------------

#----------------------------------------------------

#clik Btn ROOT?
def rootus():
    lbl = Label(del1, text="Заблокировано /ROOT: ")
    lbl.grid(column=0, row=3)

#Btn ROOT?
btn5 = Button(del1,
            text="ROOT?/ >",
            command= rootus,
            font ='Arial 8 bold',
            bg='red',
            activebackground = 'red',
            activeforeground = 'lime',
            fg="#480607"
            )
btn5.grid(column=5, row=0)

#----------------------------------------------------

#----------------------------------------------------

#clik Btn ROOT?
def BECDOR():
    from BECDORdel import socket

#Btn ROOT?
btn6 = Button(del1,
            text="BECDOR.DEL?/ >",
            command= BECDOR,
            font ='Arial 8 bold',
            bg='red',
            activebackground = 'red',
            activeforeground = 'lime',
            fg="#480607"
            )
btn6.grid(column=6, row=0)

#----------------------------------------------------

#----------------------------------------------------

#clik Btn ROOT?
def DDOSSDEL():
    from DDOSSDEL import colorama, threading, requests

#Btn ROOT?
btn7 = Button(del1,
            text="DDOSSDEL.DEL?/ >",
            command= DDOSSDEL,
            font ='Arial 8 bold',
            bg='red',
            activebackground = 'red',
            activeforeground = 'lime',
            fg="#480607"
            )
btn7.grid(column=7, row=0)

#----------------------------------------------------

#----------------------------------------------------

#clik Btn ROOT?
def IN():
    messagebox.showinfo('Информация срочно', 'Запуск консольных программ требует перезапуск системмы. \n В категорию программ входит: \n DEOS, YADER, BECDOR, DDOSSDEL. ')
    print ('Информация срочно', 'Запуск консольных программ требует перезапуск системмы. \n В категорию программ входит: \n DEOS, YADER, BECDOR, DDOSSDEL. ')

#Btn ROOT?
btn8 = Button(del1,
            text=" IN ?/ >",
            command= IN,
            font ='Arial 8 bold',
            bg='#FFCC00',
            activebackground = 'red',
            activeforeground = 'lime',
            fg="#480607"
            )
btn8.grid(column=8, row=0)

#----------------------------------------------------

del1.mainloop()
