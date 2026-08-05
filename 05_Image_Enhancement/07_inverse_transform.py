"""Inverse Transform
Image inversion, also known as negative transformation, creates the
negative of an image by reversing its pixel intensities. Dark pixels
become light and light pixels become dark.

- Converts an image into its negative representation.
- Highlights certain details that may be less visible in the original image.
- Performed by subtracting each pixel value from 255."""

import cv2
import numpy as np

image = cv2.imread(r".\images\input\cat-dog.jpg")

inverse_image = 255 - image

cv2.imwrite(".\images\output\inverse_image.jpg", inverse_image)

cv2.imshow("Original Image", image)
cv2.imshow("Inverse Image", inverse_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
