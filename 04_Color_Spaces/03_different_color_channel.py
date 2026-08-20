import cv2

image = cv2.imread(".\images\input\parrot-image.jpg")

B, G, R = cv2.split(image)
cv2.imshow("Original Image", image)
cv2.waitKey(0)

cv2.imshow("Blue Channel", B)
cv2.waitKey(0)

cv2.imshow("Green Channel", G)
cv2.waitKey(0)

cv2.imshow("Red Channel", R)
cv2.waitKey(0)

cv2.destroyAllWindows()
