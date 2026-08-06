import cv2
import numpy as np

# Read Image
image = cv2.imread("./images/input/apollo_11_launch.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Otsu Threshold
_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Morphological Closing
kernel_close = np.ones((5, 5), np.uint8)

closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_close, iterations=2)

# Morphological Opening
kernel_open = np.ones((3, 3), np.uint8)

opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel_open, iterations=1)

# Erosion (Optional)
kernel_erode = np.ones((3, 3), np.uint8)

final_mask = cv2.erode(opening, kernel_erode, iterations=1)

# Find Contours
contours, _ = cv2.findContours(final_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Empty mask
result = np.zeros_like(gray)

# Copy original image
output = image.copy()

# Draw Largest Contours
for contour in contours:

    area = cv2.contourArea(contour)

    if area > 500:
        cv2.drawContours(output, [contour], -1, (0, 255, 0), 3)
        cv2.fillPoly(result, [contour], 255)

print("Number of contours:", len(contours))

# Display Results
cv2.imshow("Original", image)
cv2.imshow("Blur", blur)
cv2.imshow("Threshold", thresh)
cv2.imshow("Closing", closing)
cv2.imshow("Opening", opening)
cv2.imshow("Final Mask", final_mask)
cv2.imshow("Detected Car", output)
cv2.imshow("Binary Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
