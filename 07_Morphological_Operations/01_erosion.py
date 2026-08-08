import cv2
import numpy as np

image = cv2.imread(r".\images\input\apollo_11_launch.jpg")

kernel = np.ones((5, 5), np.uint8)

img_erosion = cv2.erode(image, kernel, 1)

cv2.imshow("Original Image", image)
cv2.imshow("After Erosion", img_erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
