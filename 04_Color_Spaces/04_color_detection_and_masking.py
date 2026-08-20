import cv2
import numpy as np

# 1. Read the image
image = cv2.imread(".\images\input\parrot-image.jpg")

# 2. Convert BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 3. Define the lower and upper bounds for the color Green in HSV
# Hue for green is around 35-85.
# We keep Saturation and Value fairly broad to account for shadows and highlights.
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

# 4. Create the Binary Mask
# cv2.inRange checks every pixel: if it falls between our bounds, it turns it White (255). Else, Black (0).
mask = cv2.inRange(hsv_image, lower_green, upper_green)

# 5. Apply the Mask to the Original Image
# bitwise_and keeps the pixel colors from the original image ONLY where the mask is White.
result = cv2.bitwise_and(image, image, mask=mask)

# 6. Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Binary Mask", mask)
cv2.imshow("Masked Result", result)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
