from email.mime import image
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('172.20.10.9',1000))
print("Successful")
file = open('traffic_2.webp','rb')
image_data = file.read(2048)

while image_data:
    client.send(image_data)
    image_data = file.read(2048)

file.close()
client.close()
