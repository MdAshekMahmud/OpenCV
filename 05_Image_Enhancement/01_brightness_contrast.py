import cv2
import numpy as np

# Read image
image = cv2.imread(r".\images\input\cat-dog.jpg")


if image is None:
    print("Image not found")
    exit()

# Brightness & Contrast
brightness = 10
contrast = 1.5

image2 = cv2.addWeighted(
    src1=image,  # Original image
    alpha=contrast,  # Weight of first image (contrast)
    src2=np.zeros(image.shape, image.dtype),  # Second image(Black image here)
    beta=0,  # Weight of second image, 0 = Ignore src2
    gamma=brightness,  # Scalar added to every pixel (brightness)
)

# Show images
cv2.imshow("Original", image)
cv2.imshow("Brightness & Contrast", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
