import cv2, numpy

class ImageHandler():
    _greyImage : numpy.ndarray

    def __init__(self, imgPath) -> None:
        self._greyImage = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
        
    def saveImage(self):
        pass

    def resizeImage(self, width, height):
        self._greyImage = cv2.resize(self._greyImage, (width, height)) 

    def getGreyImage(self):
        return self._greyImage

    def display(self):
        cv2.imshow('image', self._greyImage)
        cv2.waitKey(0)