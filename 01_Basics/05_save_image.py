import os
import cv2

# Read image
image = cv2.imread(r".\images\input\coca-cola-logo.png")

# Save image
# output_dir = os.path.join("images", "output")
# os.makedirs(output_dir, exist_ok=True)
# output_path = os.path.join(output_dir, "saved_coca_cola_logo.png")
# cv2.imwrite(output_path, image)

cv2.imwrite("./images/output/svaed-coca-cola-logo.png", image)

print("\nImage saved successfully.")
