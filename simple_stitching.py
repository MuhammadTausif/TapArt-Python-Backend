import cv2
import numpy as np


# ============================================================================

def find_overlap_start(left_img, right_img):
    # assert left_img.shape == right_img.shape
    height, width = left_img.shape[:2]

    haystack = left_img
    needle = right_img[:, 0:width / 2]

    res = cv2.matchTemplate(haystack, needle, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    return max_loc[0]


def find_overlaps(images):
    overlap_starts = []
    for i in range(len(images) - 1):
        overlap_starts.append(find_overlap_start(images[i], images[i + 1]))
    # And the last image is used whole
    overlap_starts.append(images[-1].shape[1])
    return overlap_starts


# Simple stitch, no blending, right hand slice overlays left hand slice
def stitch_images(images, overlap_starts):
    height, width = images[0].shape[:2]
    total_width = sum(overlap_starts)
    result = np.zeros((height, total_width), np.uint8)

    current_column = 0
    for i, start in enumerate(overlap_starts):
        result[:, current_column:current_column + width] = images[i]
        current_column += start

    return result


# ============================================================================

# images = [cv2.imread("slice_%d.png" % i, 0) for i in range(4)]
# images = [cv2.imread("pano1-%d.jpeg" % i, 0) for i in range(4)]
path1 = r'D:\Users\Soft Asia\Documents\Dev\Freelancing\Fiverr\data-scrapying-py\practice\stitching\pano2-1.jpeg'
path2 = r'D:\Users\Soft Asia\Documents\Dev\Freelancing\Fiverr\data-scrapying-py\practice\stitching\pano2-2.jpeg'
path3 = r'D:\Users\Soft Asia\Documents\Dev\Freelancing\Fiverr\data-scrapying-py\practice\stitching\pano2-3.jpeg'
img1 = cv2.imread(path1, 0)
img2 = cv2.imread(path2, 0)
img3 = cv2.imread(path3, 0)
path4 = r'D:\Users\Soft Asia\Documents\Dev\Freelancing\Fiverr\data-scrapying-py\practice\stitching\second.jpg'
img4 = cv2.imread(path4)

# Displaying the image
cv2.imshow('image', img4)
cv2.imshow('image', img1)
cv2.imshow('image', img2)
cv2.imshow('image', img3)

images = [img1, img2, img3]


overlap_starts = find_overlaps(images)

cv2.imwrite("slices_out.png", stitch_images(images, overlap_starts))