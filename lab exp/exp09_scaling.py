import cv2

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")
bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow("Original", image)
cv2.imshow("Bigger (2x)", bigger)
cv2.imshow("Smaller (0.5x)", smaller)
cv2.waitKey(0)
cv2.destroyAllWindows()
