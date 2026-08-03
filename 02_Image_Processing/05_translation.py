import cv2
import numpy as np

image = cv2.imread(".\images\input\coca-cola-logo.png")


height, width = image.shape[:2]

# Translation matrix
tx = 100  # move right
ty = 50  # move down

matrix = np.float32([[1, 0, tx], [0, 1, ty]])

translated = cv2.warpAffine(image, matrix, (width, height))

cv2.imshow("Translated Image", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()
