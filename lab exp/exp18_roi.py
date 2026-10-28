import cv2

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")

# Select a region (you can change the numbers)
roi = image[50:200, 100:300]

# Paste the ROI somewhere else
image[50:200, 350:550] = roi

cv2.imshow("ROI Pasted", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
