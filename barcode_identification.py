# import in the matplotlib module
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
def capture_image():
    ''' opens camera, captures image, returns image
        use like this: new_image = capture_image()
    '''
    # open camera/capture image
    cam = cv2.VideoCapture(0)
    _,img = cam.read() # read image from camera
    cam.release() #release (close) camera
    return img

# wrapper function to decode barcodes
def decode_barcode(img):
    ''' takes in an image and returns a barcode object '''
    # decode the barcode within img and return the barcode obj
    # UPDATE THIS WITH YOUR BARCODE IDENTIFICATION CODE
    decodedObjects = pyzbar.decode(img)
    barcodeobj = decodedObjects
    return barcodeobj

# wrapper function to decode barcodes string data
def decode_barcode_data(barcode_obj):
    ''' takes in a barcode object
        returns the string text encoded in the barcode
        (data is decoded to be a type string)
    '''
    # UPDATE THIS TO PROPERLY EXTRACT AND FORMAT STRING
    for obj in barcode_obj:
        (x, y, w, h) = obj.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = obj.data
        barcodeType = obj.type

    return str(barcodeData)

# wrapper function to identify center of barcode (horizontal location)
def decode_barcode_center(barcode_obj):
    ''' takes in a barcode object
        returns the horizontal center of the barcode (int)
    '''
    # UPDATE THIS TO PROPERLY EXTRACT AND FORMAT CENTER
    for obj in barcode_obj:
        (x, y, w, h) = obj.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = obj.data
        barcodeType = obj.type
        dif=(x+w)-x
        center=x+(dif/2)
    return center


# test your code:
img = capture_image() # capture new image

# decode barcode
barcode_obj = decode_barcode(img) # send image to decode barcode

# send barcode obj to get barcode string
barcode_string = decode_barcode_data(barcode_obj)
print('Barcode string:', barcode_string)

# send barcode obj to get center of barcode
barcode_center = decode_barcode_center(barcode_obj)
print('Barcode center:', barcode_center)

# convert image for display
img = convertToRGB(img)

# display image:
plt.figure()
plt.title('Barcode Image')
plt.imshow(img) # add image to the plot
plt.show()
