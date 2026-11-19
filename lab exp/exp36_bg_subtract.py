import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Adjust these values based on your background color
lower = np.array([0, 0, 0])
upper = np.array([180, 50, 100])

mask = cv2.inRange(hsv, lower, upper)
mask_inv = cv2.bitwise_not(mask)
result = cv2.bitwise_and(image, image, mask=mask_inv)

cv2.imshow("Original", image)
cv2.imshow("Background Removed", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
