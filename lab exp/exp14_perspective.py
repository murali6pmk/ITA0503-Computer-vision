import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")
rows, cols = image.shape[:2]

pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
transformed = cv2.warpPerspective(image, matrix, (300, 300))

cv2.imshow("Original", image)
cv2.imshow("Perspective Transformed", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
