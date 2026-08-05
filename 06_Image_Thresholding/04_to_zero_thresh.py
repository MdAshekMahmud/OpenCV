# Pixels below the threshold are set to 0. Pixels above the threshold keep
# their original intensity.
import cv2
import numpy as np

image = cv2.imread(".\images\input\car.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)

_, thresh_to_zero = cv2.threshold(image, 120, 255, cv2.THRESH_TOZERO)

cv2.imshow("Binary Threshold", thresh_to_zero)

cv2.waitKey(0)
cv2.destroyAllWindows()
