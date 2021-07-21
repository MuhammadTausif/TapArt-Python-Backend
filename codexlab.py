import cv2
# print(cv2.__version__)
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("first.jpg")
img2 = cv2.imread("second.jpg")

# img_right = << your code comes here >>('/cxldata/projects/uttower_right.jpg')
# img_left = << your code comes here >>('/cxldata/projects/uttower_left.jpg')
img_right = cv2.imread("first.jpg")
img_left = cv2.imread("second.jpg")

plt.figure(figsize=(30,20))

plt.subplot(1,2,1)
plt.title("Left Image")
plt.imshow(img_left)

plt.subplot(1,2,2)
plt.title("Right Image")
plt.imshow(img_right)


plt.tight_layout()

def fixColor(image):
    return(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

img1 = cv2.cvtColor(img_right, img1)
img2 = cv2.cvtColor( img2 , cv2.COLOR_BGR2GRAY)