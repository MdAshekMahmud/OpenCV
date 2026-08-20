import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img_path = r".\images\input\apollo_11_launch.jpg"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Could not load image")
    exit()

# Apply Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(img, (5, 5), 1.5)


# Apply Canny Edge Detection
edges = cv2.Canny(blurred, 50, 150)

cv2.imshow("Original Image", img)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
