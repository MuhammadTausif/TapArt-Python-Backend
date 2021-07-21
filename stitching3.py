import cv2
import numpy as np
import matplotlib.pyplot as plt

import imageio
import imutils
path = r'D:/Users/Soft Asia/Documents/Dev/Freelancing/Fiverr/data-scrapying-py/practice/stitching/'
img1 = imageio.imread(path + "pano1-1.jpeg")
# img1 = imageio.imread("p3.jpg")
# img2 = imageio.imread("p2.jpg")
img2 = imageio.imread(path + "pano1-2.jpeg")
img3 = imageio.imread(path + "pano1-3.jpeg")

img1g = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
img2g = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols =  2, constrained_layout=False)

ax1.imshow(img1, cmap="gray")
ax1.set_xlabel("First Image", fontsize= 14)

ax2.imshow(img1, cmap="gray")
ax2.set_xlabel("Second Image", fontsize= 14)

plt.show()


def detectAndDecribe(image, method='orb'):
    if method == 'brisk':
        dit = cv2.BRISK_create()
    elif method == 'orb':
        dit = cv2.ORB_create()

    (kps, features) = dit.detectAndCompute(image, None)

    return (kps, features)


kpsA, fA = detectAndDecribe(img1g, method="brisk")
kpsB, fB = detectAndDecribe(img2g, method="brisk")

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols =  2, figsize=(20,8), constrained_layout=False)

ax1.imshow(cv2.drawKeypoints(img1g, kpsA, None, color=(0, 255, 0)))
ax1.set_xlabel("First Image", fontsize= 14)
ax2.imshow(cv2.drawKeypoints(img2g, kpsB, None, color=(0, 255, 0)))
ax2.set_xlabel("First Image", fontsize= 14)
plt.show()


def createMatcher(method, crossCheck):
    if method == 'sift' or method == 'surf':
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck = crossCheck)
    elif method == 'orb' or method == 'brisk':
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = crossCheck)
    return bf


def matchKeyPointsBF(featureA, featureB, method):
    bf = createMatcher(method, crossCheck=True)

    best_matches = bf.match(featureA, featureB)
    rawMatches = sorted(best_matches, key = lambda x:x.distance)
    return  rawMatches


