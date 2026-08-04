import cv2
import numpy as np

image = cv2.imread(r".\images\input\apollo_11_launch.jpg", cv2.IMREAD_GRAYSCALE)
# image = np.zeros((500, 500, 3), dtype=np.uint8)


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img=image, center=(x, y), radius=10, color=(0, 255, 0), thickness=-1)
        cv2.imshow("Mouse Events", image)


cv2.namedWindow("Mouse Events")
cv2.setMouseCallback("Mouse Events", mouse_event)

while True:
    cv2.imshow("Mouse Events", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
