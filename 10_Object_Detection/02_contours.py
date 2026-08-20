import cv2
import numpy as np

# 1. Load the original color image
image = cv2.imread(".\images\input\coca-cola-logo.png")

# 2. Convert to grayscale format
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# 3. Apply binary thresholding (or Canny edge detection)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 4. Find all contours in the binary image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 5. Draw the discovered boundaries onto the original image
# (-1 specifies drawing all contours; (0, 255, 0) is green; 2 is thickness)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Display the output window
cv2.imshow("Contours Visualized", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
