import cv2
import numpy as np

# 1. Create two basic binary shapes (300x300 pixels canvas)
canvas_shape = (300, 300)
square = np.zeros(canvas_shape, dtype="uint8")
circle = np.zeros(canvas_shape, dtype="uint8")

# Draw a filled white square and a filled white circle
cv2.rectangle(square, (50, 50), (250, 250), 255, -1)
cv2.circle(circle, (150, 150), 120, 255, -1)

# 2. Execute Bitwise Operations
bit_and = cv2.bitwise_and(square, circle)
bit_or = cv2.bitwise_or(square, circle)
bit_xor = cv2.bitwise_xor(square, circle)
bit_not = cv2.bitwise_not(circle)

# 3. View Results
cv2.imshow("AND (Intersection)", bit_and)
cv2.imshow("OR (Union)", bit_or)
cv2.imshow("XOR (Difference)", bit_xor)
cv2.imshow("NOT (Inversion)", bit_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
