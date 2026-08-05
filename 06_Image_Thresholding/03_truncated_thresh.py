# Pixels above the threshold take the threshold value itself. Pixels below
# the threshold remain unchanged.

import cv2
import numpy as np

image = cv2.imread(".\images\input\car.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)

_, thresh_trunc = cv2.threshold(image, 120, 255, cv2.THRESH_TRUNC)

cv2.imshow("Truncated Threshold", thresh_trunc)

cv2.waitKey(0)
cv2.destroyAllWindows()
