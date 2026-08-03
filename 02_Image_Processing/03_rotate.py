import cv2

image = cv2.imread(".\images\input\coca-cola-logo.png")

height, width = image.shape[:2]

# Rotation center
center = (width // 2, height // 2)

# Rotate 90 degree
matrix = cv2.getRotationMatrix2D(center=center, angle=90, scale=0.5)
# scale 1.0 -> same size, scale 0.5 -> half


rotated = cv2.warpAffine(image, matrix, (width, height))

cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
