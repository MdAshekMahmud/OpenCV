import cv2

image = cv2.imread(".\images\input\coca-cola-logo.png")

# Resize image
resized = cv2.resize(image, (500, 500))

# Resize using scale factor
# resized = cv2.resize(image, None, fx=0.5, fy=0.5)

cv2.imshow("Original image", image)
cv2.imshow("Resized image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
