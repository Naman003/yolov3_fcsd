import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
from tensorflow.keras.models import load_model as md
from yolov3.utils import detect_image
from yolov3.configs import *
yolo_new = md('mymod.h5',compile=False)
detect_image(yolo_new, "traffic_2.webp","pred.jpg", input_size=YOLO_INPUT_SIZE, show=True, rectangle_colors=(255,0,0))