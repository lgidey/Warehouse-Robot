import numpy as np
import matplotlib.pyplot as plt
# import in the OpenCV module
import cv2
# import pyzbar for barcode identification
import pyzbar.pyzbar as pyzbar
# function to turn barcode decoded "doorstring" into a room and direction value
N = 'N'
E = 'E'
S = 'S'
W = 'W'
def decode_barcode_data(barcode_obj):
    ''' takes in a barcode object
        returns the string text encoded in the barcode
        (data is decoded to be a type string)
    '''
    barcodeData = 0
    barcodeType = 0
    for obj in barcode_obj:
        (x,y,w,h) = obj.rect
        cv2.rectangle(img, (x,y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = obj.data
        barcodeType = obj.type

    # UPDATE THIS TO PROPERLY EXTRACT AND FORMAT STRING
    return str(barcodeData)

def parse_doorname(doorstring):
    ''' input doorstring is a string (like '11N' or '78S')
        room is an integer representing the room number (11 or 78)
        direction is a single character string ('N', 'E', 'S', 'W')
        error is False if room and direction are valid, True if error
    '''
    room = 0 # this will be updated: integer from 11 to 99
    direction = 'X' # this will be updated: 'N', 'E', 'S', 'W'
    error = False # no error
    # UPDATE CODE HERE TO DO STRING PARSING AND CHECKING
    barcode_string = decode_barcode_data(barcode_obj)
    room = int(doorstring[0:1])
    room = int(room)
    direction = doorstring[2]
    if room<11 or room>99:
        room='invalid'
        error=True
        return error
    elif direction != N:
        direction='invalid'
        error=true
        return error
    elif direction !=E:
        direction='invalid'
        error=True
        return error
    elif direction !=S:
        direction='invalid'
        error=True
        return error
    elif direction != W:
        direction = 'invalid'
        error = True
    else:
        pass

    return room, direction, error # return values

# test code
#error
room, direction, error = parse_doorname('11N') # test with 11N
print("Test 1 Room:", room, "Direction:", direction, "Error:", error)

room, direction, error = parse_doorname('78S') # test with 78S
print("Test 2 Room:", room, "Direction:", direction, "Error:", error)

# test bad strings (errors)

room, direction, error = parse_doorname('02E') # test with 02E
print("Test 3 Room:", room, "Direction:", direction, "Error:", error)

room, direction, error = parse_doorname('34X') # test with 34X
print("Test 4 Room:", room, "Direction:", direction, "Error:", error)

room, direction, error = parse_doorname('garbage') # test with 'garbage'
print("Test 5 Room:", room, "Direction:", direction, "Error:", error)
