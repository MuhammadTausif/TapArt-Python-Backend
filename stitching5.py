import cv as cv2

stitcher = cv2.createStitcher(True)

foo = cv2.imread("4.jpg")
doo = cv2.imread("5.jpg")
eoo = cv2.imread("6.jpg")
roo = cv2.imread("7.jpg")

result = stitcher.stitch((foo,doo,eoo,roo))

cv2.imshow("camera",result[1])
cv2.waitKey(0)