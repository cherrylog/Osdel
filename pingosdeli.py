import os, time
from tqdm import tqdm
import time
from colorama import Fore, Back, Style
#--------------------------------------------------------------------------------------------
print (Fore.MAGENTA + "@deliex.del/os.del")
os.system('cls')
filenames = ["img2.txt","img.txt"]
frames = []

for name in filenames:
	with open(name, "r",encoding="utf8") as f:
		frames.append(f.readlines())
		
for frame in frames:
	print ("".join(frame))
	time.sleep(1)
	os.system('cls')
#--------------------------------------------------------------------------------------------
for i in tqdm (range (100),
               desc="Подождите…",
               ascii=False, ncols=75):
    time.sleep(0.03)
        
print (Fore.MAGENTA + "\n Добро пожаловать!!! \n")

vs2 = input (Fore.MAGENTA + "Ваше имя пользователя  :    ")

print (Fore.RED + 'Ошибка проверки пользователей введите повторно ваше имя пользователя в строке Login для повторного поиска (Меры доп контроля:  )')

usrname = input (Fore.GREEN + ' Login   :     ')
if usrname == vs2 :
    for i in tqdm (range (100),
                   desc="Проверка…",
                   ascii=False, ncols=75):
        time.sleep(0.05)


else :
    print (Fore.RED + 'Неверный Login')

# Выполнение решения или компонента
print("\n")
while True:
    commandel = input(Fore.MAGENTA + "<./" + vs2 + ": \n >>>  ")
    if commandel == "ls":
        time.sleep(1)
        print(Fore.YELLOW + "\n Desctop. Dowloud. Dick-C. Games. \n")
        
    if commandel == "cmd":
        from Update import time, tqdm
        
    if commandel == "exit":
            print("выход")
            input()
            break
        
#========================== Рабочий стол ===========================================
    if commandel == "cd/Desctop.":
        time.sleep(1)
        print("\n")
        while True:
            commandel = input(Fore.MAGENTA + "<." + vs2 + "/Desktop: \n >>>  ")
            if commandel == "ls":
                print(Fore.YELLOW + "\n Command-del. Web-del. \n")
                
            if commandel == "cd/Command-del.":
                print(Fore.YELLOW + "\n Для запуска этого компонента необходимо войти вручную. \n")
                
            if commandel == "cmd":
                from Update import time, tqdm
                
            if commandel == "cmd/web.":
                print(Fore.YELLOW + "\n Command-del/Autorization/Home  ./help  ./WEB-DEL (Server) \n")
				
            if commandel == "cd":
                print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
                input()
                break
                
#=========================== Рабочий стол  ==========================================
        
#===========================   Загрузки    ==========================================
        
    if commandel == "cd/Dowloud.":
        time.sleep(1)
        while True:
            commandel = input(Fore.MAGENTA + "<." + vs2 + "/Dowloud: \n >>>  ")
            if commandel == "ls":
                print(Fore.YELLOW + "\n Home. \n")
                
            if commandel == "cmd/home":
                from login import *
                
            if commandel == "cd":
                print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
                input()
                break
        
#===========================   Загрузки    ==========================================
        
#===========================    Диск-С     ==========================================
        
    if commandel == "cd/Dick-C.":
        time.sleep(1)
        print(Fore.RED + "\n No files (ROOT ON DOSTUP & SYSTEM) \n")
        
    if commandel == "ROOT-1708":
        time.sleep(1)
        print(Fore.RED + "\n Помните что всё что вы совершаете в программном обеспечении. \n Администрация OS.DEL не несёт не какой ответственности за то что вы вводите в параграфе ROOT.")
        while True:
            commandel = input(Fore.RED + "<./ROOT /C: \n >>>  ")
            if commandel == "ls":
                print(Fore.RED + "\n Files on. \n")
                
            if commandel == "cd":
                print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
                input()
                break
        
#===========================    Диск-С     ==========================================
        
#===========================   Games.del   ==========================================
        
    if commandel == "cd/Games.":
        time.sleep(1)
        while True:
            commandel = input(Fore.MAGENTA + "<." + vs2 + "/Games.DEL: \n >>>  ")
            if commandel == "ls":
                print(Fore.YELLOW + "\n Shakgame. \n")
                
            if commandel == "cd/Shakgame.":
                from Shakgame import turtle, random, colorama
                
            if commandel == "cd":
                print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
                input()
                break
        
#===========================   Games.del   ==========================================
