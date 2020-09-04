# ALGORITHM:
# capture image
# decode barcode
# find center of barcode
# write function that compares "center of the barcode" to the "width of the image"
# determine a format for communicating how much "turning" (and which direction) is needed

import numpy as np
import matplotlib.pyplot as plt
# import in the OpenCV module
import cv2
# import pyzbar for barcode identification
import pyzbar.pyzbar as pyzbar

# convert OpenCV image to RGB for display by `matplotlib`
def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# wrapper function for capturing images
def align_robot():

    # open camera/capture image
    cam = cv2.VideoCapture(0)
    _,img = cam.read() # read image from camera
    cam.release() #release (close) camera
    img = convertToRGB(img)
    img.shape # gets the dimensions of the image
    decode_barcode(img)
    decode_barcode_data(barcode_obj)
    decode_barcode_center(barcode_obj)

    #comapre the center with how far off the robot is
    #get the center value and comapre it with max and min of the img
    rotate=0
    if 300 <= barcode_center<=340:
        rotate=0
        print('Go Straight')
    if barcode_center<300:
        diff=320-barcode_center
        rotate=1
        print('Turn left by:', diff)
    if barcode_center>340:
        diff=barcode_center-320
        rotate=-1
        print('Turn right by:', diff)

align_robot()
