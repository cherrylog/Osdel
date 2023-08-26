from tqdm import tqdm
import time
from colorama import Fore, Back, Style

# Начало приветствие
import time

print(Fore.CYAN + "       Starting Command-del ")
time.sleep(1)
print("       Loading")
time.sleep(0.5)

time.sleep(1)
print("\n       Command-del v/1.0 \n ")

time.sleep(1)
print("\n       Выбрана русская версия по умолчанию.\n ")

time.sleep(1)
print("\n       Прочитай информацию, это важно. 'information -l'\n ")

# Выбор компонента или решения

time.sleep(1)
print("\n          Для запуска введите 'su/install/start'  ")
time.sleep(1)
print("\n          Для полной устоновки введите 'su/install/update'  ")
time.sleep(1)
print("\n          Для обновления OS введите 'su/install/upgrade' \n ")
time.sleep(5)
print("\n          Полный вход в систему 'su/update/start/del/sys' \n")
time.sleep(1)
print("\n          Выход 'exit' \n ")

# Выполнение решения или компонента

while True:
    commandel = input(" 0?/: \n >>>  ")
    if commandel == "su/install/start":
        time.sleep(1)
        print("\n       Загрузка...  ")
        time.sleep(10.5)
        print("\n       Подключение к сети Del.sys...  ")
        time.sleep(5.8)
        print("\n       Успешно. \n ")
        time.sleep(5.8)
        print("\n       Для входа введите 'su/autorization/root'. \n ")
        
    if commandel == "su/update/start/del/sys":
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
        print("\n       Для продолжеия введите 'su/autorization/root' '. \n ")

    if commandel == "su/install/update":
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
        
    if commandel == "su/install/upgrade":
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
            print("OFF SYS")
            break
            
    if commandel == "information -l":
        time.sleep(1)
        print("\n       Заблокировано  \n")
        print("   Удаление файлов во время reboot \n")
        print("  Если программы не запускаются и выдают ошибку то нужно загрузить к ним компоненты в ручную, обращатся с такими вопросами к Администратору в Телеграм \n  ")
            #su/autorization/root
    if commandel == "su/autorization/root":
            from login import *
        
    if commandel == "cd/cmd":
        print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
        input()
        break

    if commandel == "su/del/cach/loocs/root/sys/ping/portinou/del":
        time.sleep(1)
        print("\n       Заблокировано  \n")
        print("   Удаление файлов во время reboot \n")

for i in tqdm (range (100),
        desc="Удаление файлов DEL … \n",
        ascii=False, ncols=75):
    time.sleep(0.05)
    print ("su/del/cach/loocs/root/sys/ping/portinou/del  \n DEL:sys/reboot")
    break
