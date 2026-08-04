import cv2

image = cv2.imread(r".\images\input\apollo_11_launch.jpg", cv2.IMREAD_GRAYSCALE)

cv2.line(image, pt1=(50, 50), pt2=(500, 500), color=(255, 0, 0), thickness=1)

cv2.imshow("Line", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
