import cv2

image = cv2.imread(r".\images\input\apollo_11_launch.jpg", cv2.IMREAD_GRAYSCALE)

# thickness = -1 for filled rectangle
cv2.rectangle(image, pt1=(100, 100), pt2=(400, 300), color=(255, 0, 2), thickness=3)

cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
