import cv2
import numpy as np
import glob
import os

logo = cv2.imread("abstract.jpg")
h_logo, w_logo, _ = logo.shape


img = cv2.imread("lennaacolored.jpg")
h_img, w_img, _ = img.shape

img2_resized = cv2.resize(img, (logo.shape[1], logo.shape[0]))
dst = cv2.addWeighted(logo, 1, img2_resized, 0.3, 0)

cv2.imshow("watermarked", dst)
cv2.waitKey(0)


print("watermrked")