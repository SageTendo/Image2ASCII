import cv2
import numpy

ASCII = "./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~# "

def encodeAs7Bit(image : numpy.ndarray):
    height, width = image.shape
    for x in range(height):
        for y in range(width):
            image[x][y] /= 4

def encodeAsAscii(image : numpy.ndarray) -> list:
    height, width = image.shape
    
    asciiImage = [ ["" for x in range(width*3)] for y in range(height*3) ]
    
    for x in range(height):
        for y in range(width):
            for i in range(4):
                asciiImage[x+i][y+i] = ASCII[image[x][y]]
    
    return asciiImage