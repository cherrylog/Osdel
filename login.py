from tqdm import tqdm
import time
import mysql.connector as mysqlconnector
import tkinter as mytk
from tkinter import *
import tkinter.messagebox as mymessagebox
from colorama import Fore, Back, Style
from tqdm import tqdm
import time

print (Fore.YELLOW + "  Добро пожаловать для подтверждения ведите свои данные и войдите на сервер...")
print ("  Введите данные о себе для проверки системы <это нужно для того что-бы системма проверила состоите ли вы в DELIEX.SYSTEM> ")
print ("  Подробнее смотрите в Telegram канале по адресу https://t.me/comandsdel \n")

log1 = input ('   Ваше имя \n ')
log2 = input ('   Ваша фомилия \n ')
log3 = input ('   Дата рождения \n ')

 
for i in tqdm (range (100),
               desc="Поиск…",
               ascii=False, ncols=75):
    time.sleep(0.10)

print ("\n ")
     
print("  Внимание сработала защита системмы !!! (Требуйтся двойная аунтитификация ).")

print ('     Войдите в системму')

MyLoginForm = mytk.Tk()
MyLoginForm.title('Вход в системму Deliex.del')
#Set Form Size
MyLoginForm.geometry("380x200")

def ClicktoLogin():
   mydb = mysqlconnector.connect(host="localhost", user="root", password="", database="osdeliex")
   mycursor = mydb.cursor(dictionary=True)
   mycursor.execute("SELECT * FROM osdel_tb where login = '"+ UserTxt.get() +"' and passwd = '"+ PassTxt.get() +"';")
   myresult = mycursor.fetchone()
   if myresult==None:
      mymessagebox.showerror("Ошибка.", "Неверно введён Login & Password")

   else:
      while True:
         from Home import tqdm, time, colorama


   mydb.close()
   mycursor.close()

# Set Tkinter Widget Size Location and Style
Bannerlabel = Label(MyLoginForm, text = "Вход в Deliex.del......", width=40, bg= 'red')
Bannerlabel.place(x=20, y=20)

UserLabel = Label(MyLoginForm, text = "login:", width=10)
UserLabel.place(x=20, y=60)

UserTxt = Entry(MyLoginForm,  width=27, relief="flat")
UserTxt.place(x=120, y=60)

#Set Focus on User Entrybox in Tkinter
UserTxt.focus()

PassLabel = Label(MyLoginForm, text = "Password :", width=10)
PassLabel.place(x=20, y=90)

PassTxt = Entry(MyLoginForm,  width=27, relief="flat")
PassTxt.place(x=120, y=90)

#Set Password Char in Entry Widget
PassTxt.config(show="*");

LoginBtn = Button(MyLoginForm, text ="< Вход >", command = ClicktoLogin, relief="groove", fg='blue')
LoginBtn.place(x=280, y=140)

MyLoginForm.configure(background='#54596d')
MyLoginForm.mainloop()
