import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
from tensorflow.keras.models import load_model as md
from yolov3.utils import detect_image
from yolov3.configs import *
import socket
import time
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('172.20.10.9',1000))
server.listen()
yolo_new = md('mymod.h5',compile=False)
print("Model is loaded and ready")
client_socket, client_address = server.accept()
file = open('recvImg.jpg','wb')
image_chunk = client_socket.recv(2048)
while True:
    # print("Inside")
    while image_chunk:
        file.write(image_chunk)
        image_chunk = client_socket.recv(2048)
    file.close()
    count = detect_image(yolo_new, file.name,"pred.jpg", input_size=YOLO_INPUT_SIZE, show=True, rectangle_colors=(255,0,0))
    # print("The number of vehicles are:",count)
    file = open('recvImg.jpg','wb')
    # print("Next")
    client_socket, client_address = server.accept()
    client_socket.sendall(bytes(str(count),'utf-8'))
    image_chunk = client_socket.recv(2048)
    # print("Received")
file.close()


