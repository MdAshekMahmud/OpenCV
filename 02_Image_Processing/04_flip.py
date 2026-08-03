import cv2

image = cv2.imread(".\images\input\coca-cola-logo.png")

# Flip horizontally
flip_horizontal = cv2.flip(image, 1)

# Flip vertically
flip_vertical = cv2.flip(image, 0)

# Flip both direction
flip_both = cv2.flip(image, -1)

cv2.imshow("Horizontal", flip_horizontal)
cv2.imshow("Vertical", flip_vertical)
cv2.imshow("Both", flip_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
