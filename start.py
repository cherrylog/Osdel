import time
from colorama import Fore
from tqdm import tqdm

time.sleep(0.1)
print(Fore.CYAN + ' Добро пожаловать!\n') # Цветной текст
time.sleep(1.0)
print(Fore.CYAN + '     Начало настройки:\n') # Цветной текст
time.sleep(1.0)
print(Fore.CYAN + '   Необходимо настроить новое виртуальное устройство.\n') # Цветной текст

vs1 = input (Fore.YELLOW + " Введите новое имя вашего ПК         (Пример 'PC-Deliexsu1288')       \n")
vs2 = input (Fore.YELLOW + " Введите имя пользователя вашего ПК  (Пример 'Nikolay')               \n")
vs3 = input (Fore.YELLOW + " Отредактируйте ОЗУ от 1GB>16GB      (Пример '8GB')                   \n")
vs4 = input (Fore.YELLOW + " Введите конфигурацию процессора     (Пример 'Intel Core I3 sys.ping')\n")

time.sleep(1.0)
print(Fore.CYAN + '   Необходимо распоковать файлы OS\n') # Цветной текст

time.sleep(1.0)
print(Fore.CYAN + ' Файлы OS: \n') # Цветной текст

time.sleep(1.0)
print(Fore.YELLOW + ' using.fix: \n') # Цветной текст
time.sleep(1.0)
print(Fore.YELLOW + ' boot.usd: \n') # Цветной текст
time.sleep(1.0)
print(Fore.YELLOW + ' lean.usd: \n') # Цветной текст
time.sleep(1.0)
print(Fore.YELLOW + ' setup.del: \n') # Цветной текст

print ('Вы согласны распаковать файлы указанные выше ? (Введите YES & NO)')

usrname = input (' setup.del   :     ')
if usrname == 'YES' :
    for i in tqdm (range (100),
                   desc="Загрузка setup.del…",
                   ascii=False, ncols=75):
        time.sleep(0.05)


else :
    print ('Такой комманды нет (Введите YES & NO)')
    
usrname = input (' using.fix   :     ')
if usrname == 'YES' :
    for i in tqdm (range (100),
                   desc="Загрузка using.fix…",
                   ascii=False, ncols=75):
        time.sleep(0.10)

else :
    print ('Такой комманды нет (Введите YES & NO)')
    
usrname = input (' boot.usd   :     ')
if usrname == 'YES' :
    for i in tqdm (range (100),
                   desc="Загрузка boot.usd…",
                   ascii=False, ncols=75):
        time.sleep(0.10)

else :
    print ('Такой комманды нет (Введите YES & NO)')
    
usrname = input (' lean.usd   :     ')
if usrname == 'YES' :
    for i in tqdm (range (100),
                   desc="Загрузка lean.usd…",
                   ascii=False, ncols=75):
        time.sleep(0.05)

else :
    print ('Такой комманды нет (Введите YES & NO)')
    
time.sleep(1.0)
print(Fore.YELLOW + ' Сборка в один файл: \n') # Цветной текст

usrname = input (' Выполнить ?   :     ')
if usrname == 'YES' :
    for i in tqdm (range (100),
                   desc="Сборка…",
                   ascii=False, ncols=75):
        time.sleep(0.05)

time.sleep(1.0)
print(Fore.YELLOW + ' Запуск OS:  (Введите Start-os) \n') # Цветной текст

while True:
    commandel = input(" <.DEL/: \n >>>  ")
    if commandel == "Start-os":
        from pingosdeli import *
        pass
		
    if commandel == "OFF":
            print("OFF SYS")
            break
# Установка и настройка OS      
