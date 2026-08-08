import cv2
import numpy as np

image = cv2.imread(r".\images\input\apollo_11_launch.jpg")

kernel = np.ones((5, 5), np.uint8)

img_dilation = cv2.dilate(image, kernel, 1)

cv2.imshow("Original Image", image)
cv2.imshow("After Erosion", img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
