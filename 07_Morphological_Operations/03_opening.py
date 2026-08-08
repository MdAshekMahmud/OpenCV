import cv2
import numpy as np

image = cv2.imread(r".\images\input\apollo_11_launch.jpg", 0)
bin = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

kernel = np.ones((3, 3), np.uint8)

opened = cv2.morphologyEx(bin, cv2.MORPH_OPEN, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("After Erosion", opened)

cv2.waitKey(0)
cv2.destroyAllWindows()
