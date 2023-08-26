import time

from colorama import Fore, Back, Style
print(Fore.WHITE + "\n")

time.sleep(1)
print("\n  Если программы не запускаются и выдают ошибку то нужно загрузить к ним компоненты в ручную, обращатся с такими вопросами к Администратору в Телеграм")

time.sleep(1)
print("И да системму лучше запускать на линукс. \n")

time.sleep(1)
print(" \n Для продолжения необходимо подтвердить вход ")

print ('Войдите в системму')

usrname = input (' Ваш log   :     ')
if usrname == 'admin' :
    print ('Выполнено ')

else :
    print ('Такого пользователя не существует!')


pasword = input (' Ваш ключ индитификации   :    ')
if pasword  == 'admin' :
    print (' Выполнено ')
    print ('Вход в системму разрешон')
    print ("Войдите в консоль своей OS на линукс и запустите сервер командой \n")
    print ("   python3 -m http.server --cgi   \n")
    time.sleep(10.1)
    print (" После чего перейдите по ссылки в крг.скобочках 'Пример: (http://0.0.0.0:8000)'")
    print(Fore.GREEN + "\n")
