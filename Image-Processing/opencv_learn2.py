'''
    grayscale and binary image
    using
        opencv-python
    aglis tech
'''
#import library
import cv2

# path gambar
path_img = "Image/baboon.png"

# load image
img_asli = cv2.imread(path_img)
cv2.imshow("asli",img_asli)
cv2.waitKey(0)
cv2.destroyWindow("asli")

# grayscale 1 imread flag 0
img_gray1 =cv2.imread(path_img,0)
cv2.imshow("grayscale flag 0",img_gray1)
cv2.waitKey(0)
cv2.destroyWindow("grayscale flag 0")

# grayscale 2 imread flag cv2.IMREAD_GRAYSCALE
img_gray2 = cv2.imread(path_img,cv2.IMREAD_GRAYSCALE)
cv2.imshow("grayscale flag imread_grayscale",img_gray2)
cv2.waitKey(0)
cv2.destroyWindow("grayscale flag imread_grayscale")

# grayscale 2 metode_cvtcolor
img_gray3 = cv2.cvtColor(img_asli,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale cvt",img_gray3)
cv2.waitKey(0)
cv2.destroyWindow("grayscale cvt")


# binary image thresh binary
img_gray = cv2.imread(path_img,0)
ret,img_binary1 = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("binary1",img_binary1)
cv2.waitKey(0)
cv2.destroyWindow("binary1")

# binary image thresh binary_inv
ret,img_binary2 = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("binary2",img_binary2)
cv2.waitKey(0)
cv2.destroyWindow("binary2")

# binary image thresh THRESH_TRUNC
ret,img_binary3 = cv2.threshold(img_gray,127,255,cv2.THRESH_TRUNC)
cv2.imshow("binary3",img_binary3)
cv2.waitKey(0)
cv2.destroyWindow("binary3")

# binary image thresh THRESH_TOZERO
ret,img_binary4 = cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO)
cv2.imshow("binary4",img_binary4)
cv2.waitKey(0)
cv2.destroyWindow("binary4")

# binary image thresh THRESH_TOZERO_INV
ret,img_binary5 = cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("binary5",img_binary5)
cv2.waitKey(0)
cv2.destroyWindow("binary5")

# binary image thresh ADAPTIVE_THRESH_MEAN_C
img_binary6 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("binary6",img_binary6)
cv2.waitKey(0)
cv2.destroyWindow("binary6")

# binary image thresh ADAPTIVE_THRESH_GAUSSIAN_C
img_binary7 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("binary7",img_binary7)
cv2.waitKey(0)
cv2.destroyWindow("binary7")

# binary image thresh THRESH_OTSU
ret,img_binary8 = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("binary8",img_binary8)
cv2.waitKey(0)
cv2.destroyWindow("binary8")