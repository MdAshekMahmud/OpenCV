"""Equalizing histograms
Histogram equalization is an image enhancement technique used to improve
image contrast by redistributing pixel intensity values. It makes details
in dark or low contrast regions more visible.

- Improves visibility of details in low contrast areas.
- Redistributes pixel intensities over a wider range.
- OpenCV provides the cv2.equalizeHist() function for histogram equalization."""

import cv2
import numpy as np

image = cv2.imread(r".\images\input\cat-dog.jpg")

if image is None:
    print("Image not found")
    exit()

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Histogram Equalization
equalized_image = cv2.equalizeHist(gray_image)

# Save image
cv2.imwrite(".\images\output\equalized.jpg", equalized_image)

cv2.imshow("Original Image", image)
cv2.imshow("Equalized Image", equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
