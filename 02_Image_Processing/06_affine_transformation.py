import cv2
import numpy as np

image = cv2.imread(".\images\input\coca-cola-logo.png")

height, width = image.shape[:2]

# Three points from original image
points1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Three corresponding points after trasnformatioin
points2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Affine transformation matrix
matrix = cv2.getAffineTransform(points1, points2)

# Apply transformation
affine = cv2.warpAffine(image, matrix, (width, height))

cv2.imshow("Affine Transformation", affine)

cv2.waitKey(0)
cv2.destroyAllWindows()
