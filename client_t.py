import socket
while True:
    name = input("Please enter filename to be stored in: ")
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('172.20.10.9',1000))
    file = open(name,'wb')
    chunk = client.recv(1024)
    while chunk:
        file.write(chunk)
        chunk = client.recv(1024)
    file.close()
    client.close()

