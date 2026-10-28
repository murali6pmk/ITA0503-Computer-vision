import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")
rows, cols = image.shape[:2]

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

matrix = cv2.getAffineTransform(pts1, pts2)
transformed = cv2.warpAffine(image, matrix, (cols, rows))

cv2.imshow("Original", image)
cv2.imshow("Affine Transformed", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
