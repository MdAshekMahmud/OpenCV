import cv2

image = cv2.imread(r".\images\input\apollo_11_launch.jpg", cv2.IMREAD_GRAYSCALE)

cv2.putText(
    image,
    text="Apollo 11 launching",
    org=(120, 250),  # Coordinates for the bottom-left corner of the text string.
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=1,
    color=(255, 0, 0),
    thickness=5,
    lineType=cv2.LINE_AA,
)

cv2.imshow("Result", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
