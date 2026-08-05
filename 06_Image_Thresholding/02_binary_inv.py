# This works opposite to the binary threshold. Pixels above the threshold
# become 0 (black), and those below become the maximum value (255;

import cv2
import numpy as np

image = cv2.imread(".\images\input\car.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)

_, thresh_binary_inv = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Binary Thresholding Inverted", thresh_binary_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()
