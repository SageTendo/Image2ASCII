import cv2, numpy

ASCII = ".'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


class ImageHandler:
    _greyImage: numpy.ndarray

    def __init__(self, imgPath):
        self._greyImage = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

    def resizeImage(self, width, height):
        self._greyImage = cv2.resize(self._greyImage, (width, height))
        return self

    def build(self):
        return self._greyImage

    def encodeAsAscii(self) -> list:
        height, width = self._greyImage.shape

        asciiImage = [["" for _ in range(width)] for _ in range(height)]
        for row in range(height):
            for col in range(width):
                asciiImage[row][col] = ASCII[self._greyImage[row][col] % len(ASCII)]
        return asciiImage
