import cv2

image = cv2.imread(r".\images\input\cat-dog.jpg")

# ksize higher means stronger blur
gaussian_blurred = cv2.GaussianBlur(src=image, ksize=(1, 1), sigmaX=0, sigmaY=0)

cv2.imshow("Original Image", image)

# Gaussian Blur
cv2.imshow("Gaussian Blurred Image", gaussian_blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
