import cv2
import numpy as np

# 1. Load image and convert to grayscale
img = cv2.imread(".\images\input\cat-dog.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Smooth the image to remove high-frequency noise
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# 3. Apply the Laplacian operator using a 64-bit float data depth
# Use cv2.CV_64F because gradients contain both positive and negative slopes
laplacian_raw = cv2.Laplacian(blurred, cv2.CV_64F, ksize=3)

# 4. Take absolute values and convert back to standard 8-bit unsigned format
laplacian_8u = np.uint8(np.absolute(laplacian_raw))

# 5. Display the output
cv2.imshow("Laplacian Edges", laplacian_8u)
cv2.waitKey(0)
cv2.destroyAllWindows()
