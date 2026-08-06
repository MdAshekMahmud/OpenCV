"""
The threshold value is not provided by us, instead, Otsu's method determines it
automatically based on the image’s histogram. This makes separation of foreground
and background particularly strong on bimodal images.
"""

import cv2

gray_image = cv2.imread(".\images\input\car.jpg", 0)

ret, otsu_thresh = cv2.threshold(
    src=gray_image, thresh=0, maxval=255, type=cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

print("\nCalculated Otsu threshold value", ret)
cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("Otsu's Thresholding", otsu_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
