import cv2

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg", 0)
_, segmented = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", image)
cv2.imshow("Segmented", segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()
