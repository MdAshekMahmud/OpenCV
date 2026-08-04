import cv2

image = cv2.imread(r".\images\input\apollo_11_launch.jpg", cv2.IMREAD_GRAYSCALE)

cv2.circle(image, center=(590, 550), radius=100, color=(56, 142, 239), thickness=-1)

cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
