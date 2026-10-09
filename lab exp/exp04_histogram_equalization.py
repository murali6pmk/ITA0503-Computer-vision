import cv2

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray)

cv2.imshow("Original Grayscale", gray)
cv2.imshow("Histogram Equalized", equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
