from email.mime import image
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('172.20.10.9',1000))
while True:
    name = input("Please enter image filename: ")
    file = open(name,'rb')
    image_data = file.read(2048)
    while image_data:
        client.send(image_data)
        image_data = file.read(2048)
    file.close()
    client.close()
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('172.20.10.9',1000))
    print(int(str(client.recv(1024),'utf-8')))
