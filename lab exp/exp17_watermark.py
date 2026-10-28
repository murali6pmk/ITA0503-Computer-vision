import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")
watermark = np.zeros_like(image)
cv2.putText(watermark, "WATERMARK", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

result = cv2.addWeighted(image, 0.7, watermark, 0.3, 0)

cv2.imshow("Original", image)
cv2.imshow("Watermarked Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
