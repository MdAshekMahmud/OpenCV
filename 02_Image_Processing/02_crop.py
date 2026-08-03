import cv2

image = cv2.imread(".\images\input\coca-cola-logo.png")

# Crop image
# image[startY:endY, startX:endX]

cropped = image[100:400, 200:500]

cv2.imshow("Original image", image)

cv2.imshow("Cropped image", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
