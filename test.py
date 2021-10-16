from gpiozero import Button
import os
import sys
from time import sleep
from PIL import Image

button = Button(23)
from picamera import PiCamera
import time

camera = PiCamera (resolution= (1920,1080),framerate = 30)
x = 3
print("Button not presseeed",)

camera.capture('back.jpg' )#, resize=(320, 240))
im = Image.open('back.jpg')
im.rotate(90).show()

while x < 10:
    if x==0:
        print("DMD0",)
        camera.start_preview(crop=(0,0,0,0),rotation=0)
        button.wait_for_press()
        button.wait_for_release()
        sleep(0.5)
        x=1
    if x==1:
        print("DMD 1 Petit")
        camera.start_preview(crop=(1860,9,55,197),rotation=0)
        button.wait_for_press()
        button.wait_for_release()
        x=2
        sleep(0.5)
    if x==2:
        print("DMD 2 Moyen",)
        camera.start_preview(crop=(1817,9,98,390),rotation=270)
        button.wait_for_press()
        button.wait_for_release()
        x=3
        sleep(0.5)
    if x==3:
        print("DMD 3 Grand",)
        camera.start_preview(crop=(1764,9,152,582),rotation=0,fullscreen=False, window = (0, 0, 500, 1920))
        button.wait_for_press()
        button.wait_for_release()
        x=0
        sleep(0.5)
#print("Fin")


