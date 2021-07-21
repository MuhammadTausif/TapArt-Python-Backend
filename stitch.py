# import the necessary packages
from practice.stitching.panaroma import Stitcher
import argparse
import imutils
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="pano1-1.jpeg")
ap.add_argument("-s", "--second", required=True,
	help="pano1-2.jpeg")
# ap.add_argument("-f", "--first", required=True,
# 	help="path to the first image")
# ap.add_argument("-s", "--second", required=True,
# 	help="path to the second image")
# args = vars(ap.parse_args())
# args = vars(ap.parse_args())


# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
# imageA = cv2.imread(args["first"])
# imageB = cv2.imread(args["second"])
imageA = cv2.imread('pano1-1.jpeg')
imageB = cv2.imread("pano1-2.jpeg")
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)
# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)