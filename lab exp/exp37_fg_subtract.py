import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Adjust these values based on the object color you want to remove
lower = np.array([0, 50, 50])
upper = np.array([120, 255, 255])

mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original", image)
cv2.imshow("Foreground Only", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
