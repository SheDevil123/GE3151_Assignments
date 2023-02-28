import random
from timeit import default_timer as timer
import threading
import face_recognition
import cv2

def img1():
    img_bgr = face_recognition.load_image_file('Kharghuvel.jpg')
    img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
    kharghuvel_enc = face_recognition.face_encodings(img_rgb)[0]

def img2():
    img_bgr = face_recognition.load_image_file('real.jpg')
    img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
    real_enc = face_recognition.face_encodings(img_rgb)[0]

start=timer()
img1()
img2()
print(timer()-start)
start=timer()

t1=threading.Thread(target=img1)
t2=threading.Thread(target=img2)
t1.start()
t2.start()
t1.join()
t2.join()
print(timer()-start)