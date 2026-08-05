import cv2
import numpy as np

image = cv2.imread(r".\images\input\cat-dog.jpg")


sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

sharpened_image = cv2.filter2D(src=image, ddepth=-1, kernel=sharpen_kernel)


cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
