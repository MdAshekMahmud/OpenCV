"""Noise Reduction
Noise reduction is an image enhancement technique used to remove unwanted
noise and improve image quality. It helps create smoother images while
preserving important details.

- Makes images easier to analyze and process.
- OpenCV provides filters such as Median Blur and Gaussian Blur for noise reduction.
- The cv2.medianBlur() function is particularly effective for removing salt-and-pepper noise.
"""

import cv2

image = cv2.imread(r".\images\input\cat-dog.jpg")

gaussian_blurred = cv2.GaussianBlur(src=image, ksize=(1, 1), sigmaX=0, sigmaY=0)
median_blurred = cv2.medianBlur(src=image, ksize=3)


cv2.imshow("Original Image", image)
# Gaussian Blur
cv2.imshow("Gaussian Blurred Image", gaussian_blurred)
# Median Blur
cv2.imshow("Median Blurred Image", median_blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
