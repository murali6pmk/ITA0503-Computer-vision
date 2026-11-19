import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)
closed = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original", gray)
cv2.imshow("Closing", closed)
cv2.waitKey(0)
cv2.destroyAllWindows()
