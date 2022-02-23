import socket
import time
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('172.20.10.9',1000))
server.listen()
while True:
    client_socket, client_address = server.accept()
    file = open('server_2.py','rb')
    chunk = file.read(2048)
    while chunk:
        client_socket.send(chunk)
        chunk = file.read(2048)
    file.close()



