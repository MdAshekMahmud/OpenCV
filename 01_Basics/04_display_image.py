import cv2

# Read Image
image = cv2.imread(".\images\input\coca-cola-logo.png")

# Diaplay image
cv2.imshow("Coca Cola", image)

# Wait until key press
cv2.waitKey(0)

# Close window
cv2.destroyAllWindows()
