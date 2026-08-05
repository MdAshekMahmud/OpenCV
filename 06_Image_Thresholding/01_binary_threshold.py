# If a pixel’s intensity is above the threshold, it is assigned the maximum value
# (usually 255; white)—otherwise, it becomes 0 (black).

import cv2
import numpy as np

image = cv2.imread(".\images\input\car.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)

_, thresh_binary = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary Threshold", thresh_binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
