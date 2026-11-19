import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))
text = input("Enter the text to display: ")

image = np.ones((height, width, 3), dtype=np.uint8) * 255
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, text, (50, height//2), font, 1, (0, 0, 255), 2)

cv2.imshow("Text Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
