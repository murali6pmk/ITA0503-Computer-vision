import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg", 0)
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(image, kernel, iterations=1)

cv2.imshow("Original", image)
cv2.imshow("Dilation", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
