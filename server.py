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
server.bind(('localhost',1000))
server.listen()
print("Before")
client_socket, client_address = server.accept()
file = open('recvImg.jpg','wb')
image_chunk = client_socket.recv(2048)
print("First")
while True:
    while image_chunk:
        file.write(image_chunk)
        image_chunk = client_socket.recv(2048)
    yolo_new = md('mymod.h5',compile=False)
    name = file.name
    file.close()
    detect_image(yolo_new,name,"pred.jpg", input_size=YOLO_INPUT_SIZE, show=True, rectangle_colors=(255,0,0))
    client_socket, client_address = server.accept()
    image_chunk = client_socket.recv(2048)
    file = open('recvImg.jpg','wb')
file.close()
