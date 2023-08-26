import sys
import os
from imageHandler import ImageHandler

if __name__ == "__main__":
    # Get the file path from CLI args
    filepath = sys.argv[1]
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <image filepath>")

    # Get terminal dimensions
    term_width, term_height = os.get_terminal_size()

    # Get the image from the filepath
    image_handler = ImageHandler(filepath)

    # Resize the image to the terminal's dimensions and get the ASCII encoding
    asciiImage = (image_handler
                  .resizeImage(term_width, term_height)
                  .encodeAsAscii())

    # Print to the console
    for row in range(len(asciiImage)):
        for col in range(len(asciiImage[0])):
            print(asciiImage[row][col], end="")
        print()
