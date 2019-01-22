'''
    code for load and show image
    with : 
        opencv
    by aglissae
'''

# import library
import cv2

# load image
image = cv2.imread("Image/baboon.png")

# check matrik gambar
# print(image)

# show image
cv2.imshow("gambar baboon",image)
cv2.waitKey()
