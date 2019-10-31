pip install pytesseract
pip install opencv
pip install tox
pip install pillow

# import the necessary packages
from PIL import Image
import pytesseract
import cv2
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# load the example image and convert it to grayscale
image = cv2.imread("Enter your image path.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", gray)

# check to see if we should apply thresholding to preprocess the image
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# write the grayscale image to disk as a temporary file so we can apply OCR to it
filename = "{}.png".format(os.getpid()) #to derive a temporary image filename
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
text = pytesseract.image_to_string(Image.open(filename)) 
os.remove(filename) #cleanup
print(text)

# show the output images
cv2.imshow("Output image", gray)
cv2.waitKey(0) 
