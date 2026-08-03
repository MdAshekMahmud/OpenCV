import cv2

image = cv2.imread(".\images\input\coca-cola-logo.png")

# Print image matrix
print(image)

# Access single pixel (B, G, R)
pixel = image[100][100]

print("Pixel value: ", pixel)
