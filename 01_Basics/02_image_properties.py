import cv2

image = cv2.imread(".\images\input\coca-cola-logo.png")


# Image properties
print("\nShape: ", image.shape)
print("Height: ", image.shape[0])
print("Width: ", image.shape[1])
print("Channels: ", image.shape[2])

# Data type
print("\nData Tyep: ", image.dtype)

# Total pixels
print("\nTotal Pixels: ", image.size, "\n")
