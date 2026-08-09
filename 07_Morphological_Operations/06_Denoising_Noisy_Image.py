import cv2

image = cv2.imread(r".\images\input\apollo_11_launch.jpg", 0)

dst = cv2.fastNlMeansDenoising(image, None, 10, 7, 15)
cv2.imshow("Denoised Image", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
