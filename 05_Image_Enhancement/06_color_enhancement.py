import cv2
import numpy as np

import cv2

image = cv2.imread(r".\images\input\cat-dog.jpg")

if image is None:
    print("Image not found")
    exit()

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Adjust Hue, Saturation, and Value
hsv[:, :, 0] = np.clip(hsv[:, :, 0] * 0.7, 0, 179)  # Change Hue (color tone)
hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.5, 0, 255)  # Increase Saturation (more vivid)
hsv[:, :, 2] = np.clip(hsv[:, :, 2] * 0.5, 0, 255)  # Decrease Brightness (darker image)

# Convert HSV back to BGR
image2 = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Save image
cv2.imwrite(".\images\output\enhanced-coloured.jpg", image2)

cv2.imshow("Original Image", image)
cv2.imshow("Enhanced Colour", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
