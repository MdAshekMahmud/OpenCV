"""
Adaptive Mean Thresholding
- The threshold for each pixel is computed as the mean value of the surrounding block
  (199x199 neighborhood, here), minus the constant (5).
- Best for images with fairly consistent noise or lighting within local regions.

Adaptive Gaussian Threosholding
- The threshold for each pixel comes from a weighted sum of surrounding pixels
  (Gaussian window), minus the constant (5).
- More effective than mean in regions with gradual intensity variations.
"""

import cv2

gray_image = cv2.imread(".\images\input\car.jpg", 0)

#  Adaptive Mean Thresholding
thresh_mean = cv2.adaptiveThreshold(
    src=gray_image,
    maxValue=255,
    adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
    thresholdType=cv2.THRESH_BINARY,
    blockSize=199,
    C=5,
)

thresh_gauss = cv2.adaptiveThreshold(
    src=gray_image,
    maxValue=255,
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    thresholdType=cv2.THRESH_BINARY,
    blockSize=199,
    C=5,
)

cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("Adaptive Mean Thresholding", thresh_mean)
cv2.imshow("Adaptive Gaussian Thresholding", thresh_gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()
