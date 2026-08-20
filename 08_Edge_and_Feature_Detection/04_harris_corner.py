import cv2
import numpy as np

# 1. Load the target image
image = cv2.imread(".\images\input\cat-dog.jpg")
original = image.copy()

# 2. Convert to grayscale (Harris detector requires intensity variations)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Convert to float32 (Required format for the algorithm)
gray = np.float32(gray)

# 4. Apply Harris Corner Detection
# Parameters: input image, neighborhood size, Sobel aperture, Harris free parameter
dst = cv2.cornerHarris(src=gray, blockSize=2, ksize=3, k=0.04)

# 5. Dilate the results to make the corner points visible
dst = cv2.dilate(dst, None)

# 6. Thresholding: Mark corners in red [0, 0, 255] where response is above 1% of max
image[dst > 0.01 * dst.max()] = [0, 0, 255]

# 7. Display results
cv2.imshow("Original Image", original)
cv2.imshow("Detected Corners", image)

if cv2.waitKey(0) & 0xFF == 21:
    cv2.destroyAllWindows()
