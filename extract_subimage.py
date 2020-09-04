import random
import numpy as np
import matplotlib.pyplot as plt
# inport in the OpenCV module
import cv2

img=new_img

# cam = cv2.VideoCapture(0)
# _,img = cam.read() # read image from camera
# cam.release() #release (close) camera
# # convert image for display
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
x_min=0
y_min=0
x_max=0
y_max=0

def check_color(x,y,img):
    LR=70
    UR=98
    LG=110
    UG=140
    LB=50
    UB=100

    R=img[x,y][0]
    G=img[x,y][1]
    B=img[x,y][2]
    if LR<=R<=UR:
        if LG<=G<=UG:
            if LB<=B<=UB:
                return True

    return False

H=img.shape[0]
W=img.shape[1]

for x in range (H-1):
    y=int(W/2)
    if not check_color(x,y, img):
        if not check_color(x+1,y, img):
            x_min=x
            break
for x in reversed(range(H-1)):
    y=int(W/2)
    if not check_color(x,y, img):
        if not check_color(x-1,y, img):
            x_max=x
            break

for y in range (W-1):
    x=int(H/2)
    if not check_color(x,y, img):
        if not check_color(x,y+1, img):
            y_min=y
            break
for y in reversed(range(W-1)):
    x=int(H/2)
    if not check_color(x,y, img):
        if not check_color(x,y-1, img):
            y_max=y
            break

new_img=img[x_min:x_max, y_min:y_max]
plt.figure()
plt.imshow(new_img)
plt.show()
