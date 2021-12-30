from numpy import array
from numpy.lib.type_check import imag
from imageHandler import ImageHandler
import imageProcessor

if __name__ == '__main__':
    filepath = str(input("Enter filepath: "))

    imgHandler = ImageHandler(filepath)
    image = imgHandler.getGreyImage()
    imageProcessor.encodeAs7Bit(image)
    asciiImage = imageProcessor.encodeAsAscii(image)

    f = open('ascii.txt', 'w')

    for x in range(len(asciiImage)):
        for y in range(len(asciiImage[0])):
            f.write(asciiImage[x][y])
        f.write('\n')
    
    f.close()
