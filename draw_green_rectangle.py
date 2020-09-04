import random
import numpy as np
import matplotlib.pyplot as plt
# import in the OpenCV module
import cv2
# UPDATE THESE TO BE RANDOMLY PICKED
# hint 1: use img.shape to identify your max values
# hint 2: if randomly picking values, make sure
# your x2, y2 are bigger than your x1, y1!

cam = cv2.VideoCapture(0)
_,img = cam.read() # read image from camera
cam.release() #release (close) camera
# convert image for display
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

x=img.shape[0] # gets the dimnesions
y=img.shape[1]

# top left (x1, y1):
x1 = 10
y1 = 10
# bottom right (x2, y2):
x2 = 630
y2 = 470

x1 = random.randint(1,x)
y1 = random.randint(1,y)
x2 = random.randint((x1+1),(x-x1))
y2 = random.randint((y1+1),y-y1)
# use for loop to draw the rectangle on top of the img

cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 10)


# draw green rectangle on top of it

plt.figure()
plt.imshow(img)
plt.show()
