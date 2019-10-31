# USAGE
#pyhton ocr.py --image images/example_01.png 
#python ocr.py --image images/example_02.png  --preprocess blur

#pip install pytesseract
#pip install opencv
#pip install tox
#pip install pillow

# import the necessary packages
from PIL import Image
import pytesseract
import cv2
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# load the example image and convert it to grayscale
image = cv2.imread("C:\\Users\\dhruv\\Desktop\\tesseract-python\\images\\example_03.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", gray)

# check to see if we should apply thresholding to preprocess the image
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#threshold will give binary values to the pixels of the image

# write the grayscale image to disk as a temporary file so we can apply OCR to it
filename = "{}.png".format(os.getpid()) #to derive a temporary image filename
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
text = pytesseract.image_to_string(Image.open(filename)) #convert the contents of the image into our desired string
os.remove(filename) #cleanup
print(text)

# show the output images
cv2.imshow("Output image", gray)
cv2.waitKey(0) #wait until a key on the keyboard is pressed before exiting the script