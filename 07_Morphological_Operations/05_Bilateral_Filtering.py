import cv2

image = cv2.imread(r".\images\input\apollo_11_launch.jpg", 0)

bilateral = cv2.bilateralFilter(image, 15, 75, 75)
cv2.imshow("Apollo 11 Launching", bilateral)


cv2.waitKey(0)
cv2.destroyAllWindows()
