from tqdm import tqdm
import time
from colorama import Fore, Back, Style

# Выполнение решения или компонента
print(Fore.GREEN + "\n")
while True:
    commandel = input(" <.DEL-HOME/: \n >>>  ")
    if commandel == "help":
        time.sleep(1)
        print(Fore.YELLOW + "\n")
        print("\n       Мой ключ доступа             'su/del/set/my_codes'")
        print("\n       Yader                        'su/del/programms -y /yader-del/start'")
        print("\n       DDOSSDEL                     'su/del/programms -y /ddos-del/start'")
        print("\n       Textdelus                    'su/del/systemm/rf/conf -L /nem/Textdelus'")
        print("\n       Fileprog                     'su/del/systemm/rf/file -y /nem/Fileprog'")
        print("\n       Остановка системы.           'OFF'  ")
        print("\n       Перезагрузка.                'reboot'  ")
        print("\n       WEB-DEL (Server)             'su/del/programms -y /web-del/start/server.sys'")
        print("\n       Перезагрузится в OS.del      'reboot/Os-del'")
        print("\n       DEOS                         'sys/deos/root/ping/sys32/admin/admin/  deos.del'")
        print(Fore.GREEN + "\n")

    if commandel == "su/del/set/my_codes":
        time.sleep(1)
        print (Fore.MAGENTA + "\n    1985-7635-6453-6253-8732 del-console /my_admin /pass_admin")
        print(Fore.GREEN + "\n")

    if commandel == "su/del/programms -y /yader-del/start":
        from Yader import time

    if commandel == "su/del/programms -y /ddos-del/start":
        from Ddosdel import colorama, threading, requests

    if commandel == "sys/deos/root/ping/sys32/admin/admin/  deos.del":
        from Dbpy.main import pymysql
        
    if commandel == "su/del/systemm/rf/conf -L /nem/Textdelus":
        from Textdelsu import messagebox, filedialog

    if commandel == "su/del/programms -y /web-del/start/server.sys":
        from webdel.Server.Start.Startwebdel import time

    if commandel == "su/del/systemm/rf/file -y /nem/Fileprog":
        from Fileprog import messagebox, time

    if commandel == "OFF":
            print(Fore.RED +"OFF SYS")
            print(Fore.GREEN + "\n")
            break
            
    if commandel == "reboot/Os-del":
        print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
        input()
        from pingosdeli import os, time, tqdm, colorama

    if commandel == "reboot":
        from Update import tqdm, time
